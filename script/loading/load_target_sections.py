import configparser
import logging
import sqlite3
from sqlite3 import Error
from script.helper.helper2 import *
import sys
import os
import shutil
import pandas
from script.helper.extractor import *
    
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    readme_file_dir = config['DEFAULT']['target_readme_file_dir']
    temp_abstracted_markdown_file_dir = config['DEFAULT']['temp_target_abstracted_markdown_file_dir']
    
    log_filename = '../../log/load_target_sections.log'
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    # Extract heading
    overview = extract_headings_from_files_in_directory(readme_file_dir)
        
    conn = sqlite3.connect(db_filename)
    try:
        c = conn.cursor()
        logging.info("Saving section overviews to database")
        # Delete existing data
        c.execute('DELETE FROM target_section_overview')
        conn.commit()
        overview.to_sql(name='target_section_overview', con = conn, if_exists='append', index=False)
        conn.commit()        
        logging.info("Section headings loaded")

        # Extract section content
        logging.info("Loading section content")
        # Delete existing data
        result = c.execute('DELETE FROM target_section_content')
        if (not temp_abstracted_markdown_file_dir.startswith('../../temp')):
            logging.info('Please ensure that temp_abstracted_markdown_file_dir config variable is set correctly')
            sys.exit()
        else:
            shutil.rmtree(temp_abstracted_markdown_file_dir,ignore_errors=True)
            os.mkdir(temp_abstracted_markdown_file_dir)
        logging.info("Fetching list of distinct filenames")
        
        result = c.execute("""
            SELECT DISTINCT local_readme_file
            FROM target_section_overview 
            ORDER BY file_id""")
        
        filenames = result.fetchall()
        conn.commit()
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()
        
    abstract_out_markdown(filenames, readme_file_dir, temp_abstracted_markdown_file_dir)
    extract_section_from_abstracted_files_v2(temp_abstracted_markdown_file_dir, db_filename, 'target_section_overview','target_section_content')
    logging.info("Operation completed")