'''
Identify and extract headings from README file whose sections are to be classified.
'''
import configparser
import logging
import pandas
from pandas import DataFrame
from script.helper.helper2 import *
import sqlite3
from sqlite3 import Error
from script.helper.extractor import *

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    target_readme_file_dir = config['DEFAULT']['target_readme_file_dir']
    temp_target_abstracted_markdown_file_dir = config['DEFAULT']['temp_target_abstracted_markdown_file_dir']
    
    log_filename = '../../log/load_target_section_overview.log'    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    overview = extract_headings_from_files_in_directory(target_readme_file_dir)
        
    conn = sqlite3.connect(db_filename)
    try:
        c = conn.cursor()
        logging.info("Saving section overviews to database")
        # Delete existing data
        c.execute('DELETE FROM target_section_overview')
        conn.commit()
        overview.to_sql(name='target_section_overview', con = conn, if_exists='append', index=False)
        conn.commit()
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()
        
    logging.info("Operation completed")    
                    
    