'''
@author: gprana
'''
import configparser
from helper import helper2, extractor
import logging
import sqlite3

if __name__ == '__main__':    
    log_filename = '../log/load_dev_and_eval_datasets.log'
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    
    config = configparser.ConfigParser()
    config.read('../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    readme_file_dir = config['DEFAULT']['readme_file_dir']
    temp_abstracted_markdown_file_dir = config['DEFAULT']['temp_abstracted_markdown_file_dir']
    
    for n in ['25','75']:
        logging.info(f'Emptying tables for {n} pct data')
        conn = sqlite3.connect(db_filename)
        # Delete existing data
        c = conn.cursor()
        c.execute(f'DELETE FROM section_overview_{n}pct')
        c.execute(f'DELETE FROM section_content_{n}pct')
        conn.commit()
        logging.info('Cleanup completed')
        
        input_filename_csv = config['DEFAULT'][f'section_overview_{n}pct_filename']
        logging.info(f'Processing files from {input_filename_csv}')
        extractor.load_section_overview_from_csv(input_filename_csv, db_filename, f'section_overview_{n}pct')
        filenames = extractor.retrieve_readme_filenames_from_db(db_filename, f'section_overview_{n}pct')
        logging.info(f'Processing README file. Using {temp_abstracted_markdown_file_dir} for temp storage')
        extractor.delete_existing_section_content_data(temp_abstracted_markdown_file_dir, db_filename, f'section_content_{n}pct')
        extractor.abstract_out_markdown(filenames, readme_file_dir, temp_abstracted_markdown_file_dir)
        extractor.extract_section_from_abstracted_files(temp_abstracted_markdown_file_dir, db_filename, 
                                              f'section_overview_{n}pct',
                                              f'section_content_{n}pct')
        logging.info(f'Finished loading data for {n} pct set')
    logging.info('Operation completed')