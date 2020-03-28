import configparser
from helper.helper2 import *
import logging
from helper.extractor import *
import time
        
if __name__ == '__main__':
    start = time.time()
    
    config = configparser.ConfigParser()
    config.read('../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    input_filename_csv = config['DEFAULT']['section_overview_combined_filename']
    readme_file_dir = config['DEFAULT']['readme_file_dir']
    temp_abstracted_markdown_file_dir = config['DEFAULT']['temp_abstracted_markdown_file_dir']
    log_filename = '../log/load_section_dataset_combined.log'
    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    load_section_overview_from_csv(input_filename_csv, db_filename, 'section_overview_combined')
    filenames = retrieve_readme_filenames_from_db(db_filename, 'section_overview_combined')
    delete_existing_section_content_data(temp_abstracted_markdown_file_dir, db_filename, 'section_content_combined')
    abstract_out_markdown(filenames, readme_file_dir, temp_abstracted_markdown_file_dir)
    extract_section_from_abstracted_files(temp_abstracted_markdown_file_dir, db_filename, 'section_overview_combined','section_content_combined')
    
    end = time.time()
    runtime_in_seconds = end - start
    logging.info('Operation completed in {0}'.format(runtime_in_seconds))