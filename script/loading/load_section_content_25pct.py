import configparser
import logging
import sqlite3
from sqlite3 import Error
import sys
import os
import shutil
import pandas
from script.helper.extractor import *

    
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    readme_file_dir = config['DEFAULT']['readme_file_dir']
    log_filename = '../../log/load_section_content_25pct.log'
    temp_abstracted_markdown_file_dir = config['DEFAULT']['temp_abstracted_markdown_file_dir']
    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    conn = sqlite3.connect(db_filename)
    try:
        c = conn.cursor()
        logging.info("Cleaning existing data")
        result = c.execute('DELETE FROM section_content_25pct')
        if (not temp_abstracted_markdown_file_dir.startswith('../../temp')):
            logging.info('Please ensure that temp_abstracted_markdown_file_dir config variable is set correctly')
            sys.exit()
        else:
            shutil.rmtree(temp_abstracted_markdown_file_dir)
            os.mkdir(temp_abstracted_markdown_file_dir)
        logging.info("Fetching list of distinct filenames")
        
        result = c.execute("""
            SELECT DISTINCT local_readme_file
            FROM section_overview_25pct 
            ORDER BY file_id, section_id""")
        
        filenames = result.fetchall()
        conn.commit()
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()
        
    abstract_out_markdown(filenames, readme_file_dir, temp_abstracted_markdown_file_dir)
    extract_section_from_abstracted_files(temp_abstracted_markdown_file_dir, db_filename, 'section_overview_25pct','section_content_25pct')