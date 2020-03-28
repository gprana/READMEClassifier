import configparser
import logging
import sqlite3
from sqlite3 import Error
from helper import helper2
import sys
import os
import shutil
import pandas
from helper import extractor
    
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    readme_file_dir = config['DEFAULT']['target_readme_file_dir']
    temp_abstracted_markdown_file_dir = config['DEFAULT']['temp_target_abstracted_markdown_file_dir']
    
    log_filename = '../log/load_target_sections.log'
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    # Extract heading
    overview = extractor.extract_headings_from_files_in_directory(readme_file_dir, db_filename, 'target_section_overview')    
    
    filenames = extractor.retrieve_readme_filenames_from_db(db_filename, 'target_section_overview')
    extractor.delete_existing_section_content_data(temp_abstracted_markdown_file_dir, db_filename, 'target_section_content')
    extractor.abstract_out_markdown(filenames, readme_file_dir, temp_abstracted_markdown_file_dir)
    extractor.extract_section_from_abstracted_files_v2(temp_abstracted_markdown_file_dir, db_filename, 'target_section_overview','target_section_content')
    logging.info("Operation completed")