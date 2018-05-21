import configparser
import pandas as pd
import sys
import codecs
import sqlite3
from script.helper.helper2 import *
import logging

def merge_classes_1_and_2(code_string):
    code_string = code_string.replace('2','1')
    code_csv = ','.join([d for d in code_string])
    return code_csv

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    input_filename = config['DEFAULT']['section_overview_25pct_filename']
    log_filename = '../../log/load_section_overview_25pct.log'
    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    df = pd.read_csv(input_filename, header=0, delimiter=',',
                     names=['section_id','file_id','url','heading_markdown','section_code'])
    
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    
    readme_file_generator = lambda x: x.replace('https://github.com/','').replace('/','.') + '.md'
    df['local_readme_file'] = df['url'].apply(readme_file_generator) 
    df['heading_text'] = df['heading_markdown'].apply(extract_text_in_heading_markdown)
    # In markdown, # = heading level 1, ## = heading level 2, etc.
    df['heading_level'] = df['heading_markdown'].apply(lambda x : len(re.search('^#+', x).group(0)))
    df['abstracted_heading_markdown'] = df['heading_markdown'].apply(lambda x : abstract_text(x).replace('\n', ' ').strip())
    df['abstracted_heading_text'] = df['abstracted_heading_markdown'].apply(extract_text_in_heading_markdown)
    # Don't convert to int, as data contains '-' for 'not in any class'
    df['section_code'] = df['section_code'].apply(lambda x : merge_classes_1_and_2(x))
    
    try:
        logging.info('Emptying table and loading overviews')
        conn = sqlite3.connect(db_filename)
        # Delete existing data
        c = conn.cursor()
        c.execute('DELETE FROM section_overview_25pct')
        conn.commit()
        df.to_sql('section_overview_25pct', conn, if_exists='append', index=False)
        logging.info('Loading completed')
        logging.info(df.shape)
        logging.info('Deleting entries with only \'##\' as text')
        # Delete '##' entries that correspond to horizontal lines and are all labeled as '-'
        c.execute('DELETE FROM section_overview_25pct WHERE heading_markdown=\'##\'')
        conn.commit()
        logging.info('Operation completed')
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()