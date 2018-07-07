import configparser
import logging
import pandas
from pandas import DataFrame
import numpy as np
import sqlite3
from sqlite3 import Error
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.cross_validation import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from script.helper.heuristic2 import *
from script.helper.balancer import *
import time
import operator
from sklearn.externals import joblib
from sklearn.calibration import CalibratedClassifierCV

if __name__ == '__main__':
    start = time.time()
    
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    rng_seed = int(config['DEFAULT']['rng_seed'])
    vectorizer_filename = config['DEFAULT']['vectorizer_filename'] 
    binarizer_filename = config['DEFAULT']['binarizer_filename'] 
    model_filename = config['DEFAULT']['model_filename'] 
    log_filename = '../../log/classifier_train_model_predict_proba.log'
    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    conn = sqlite3.connect(db_filename)
    try:
        sql_text1 = """
        SELECT t1.file_id, t1.section_id, t1.url, t1.heading_text, t2.content_text_w_o_tags, 
        t1.abstracted_heading_text || ' ' || t2.content_text_w_o_tags AS abstracted_heading_plus_content, 
        t1.section_code
        FROM section_overview_combined t1 
        JOIN section_content_combined t2 
        ON t1.file_id=t2.file_id AND t1.section_id=t2.section_id
        """
        df = pandas.read_sql_query(con=conn, sql=sql_text1)
        
        df_randomized_order = df.sample(frac=1, random_state=rng_seed)
        heading_plus_content_corpus = df_randomized_order['abstracted_heading_plus_content']
        content_corpus = df_randomized_order['content_text_w_o_tags']
        heading_text_corpus = df_randomized_order['heading_text']
        url_corpus = df_randomized_order['url']
        
        # Class '2' has been merged into class '1'
        label_set = ['-','1','3','4','5','6','7','8']
        labels = [str(x).split(',') for x in df_randomized_order['section_code']]
        mlb = MultiLabelBinarizer(classes=label_set)
        labels_matrix = mlb.fit_transform(labels)
        
        tfidf = TfidfVectorizer(ngram_range=(1,1), analyzer='word', stop_words='english')
        tfidfX = tfidf.fit_transform(heading_plus_content_corpus)
        
        logging.info('tfidf matrix shape: ')  
        logging.info(tfidfX.shape)
        
        # Derive features from heading text and content
        logging.info('Deriving features')
        derived_features = derive_features_using_heuristics(url_corpus, heading_text_corpus, content_corpus)
                
        logging.info('Derived features shape:')
        logging.info(derived_features.shape)
                
        features_tfidf = pandas.DataFrame(tfidfX.todense())
        # Assign column names to make it easier to print most useful features later
        features_tfidf.columns = tfidf.get_feature_names()
        features_combined = pandas.concat([features_tfidf, derived_features], axis=1)
        
        logging.info('Combined features shape:')
        logging.info(features_combined.shape)
        
        svm_object = LinearSVC() 
        clf = CalibratedClassifierCV(svm_object) 
        classifier = OneVsRestClassifierBalance(clf)
        
        logging.info('Training classifier')
        classifier.fit(features_combined.values, labels_matrix) 
        logging.info('Saving TFIDF vectorizer')
        joblib.dump(tfidf, vectorizer_filename)
        logging.info('Saving binarizer')
        joblib.dump(mlb, binarizer_filename)
        logging.info('Saving model')
        joblib.dump(classifier, model_filename)
                
        end = time.time()
        runtime_in_seconds = end - start
        logging.info('Processing completed in {0}'.format(runtime_in_seconds))
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()