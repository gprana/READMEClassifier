'''
Identify and extract headings from README file whose sections are to be classified. Takes unprocessed README files as input. 
This allows headings such as "Section 2", "Section 3", etc. to be extracted as is first for later reference / manual checking 
(instead of having everything turned into "Section @abstr_number").
To reduce false positives (lines starting with # that isn't actually a heading, such as comment lines in code snippets), 
abstract out code section blocks.
'''
import configparser
import logging
import pandas
from pandas import DataFrame
from script.helper.helper2 import *
import sqlite3
from sqlite3 import Error
import os

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    target_readme_file_dir = config['DEFAULT']['target_readme_file_dir']
    temp_target_abstracted_markdown_file_dir = config['DEFAULT']['temp_target_abstracted_markdown_file_dir']
    
    log_filename = '../../log/load_target_section_overview.log'    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    overview = DataFrame(columns=['section_id', 'file_id', 'url', 'local_readme_file', 'heading_markdown',
                                  'abstracted_heading_markdown', 'heading_text', 'abstracted_heading_text',
                                  'heading_level'])
    
    file_id = 1
    for filename in os.listdir(target_readme_file_dir):
        # Used to construct the repo URL later
        filename_w_o_ext = os.path.splitext(filename)[0]
        s = filename_w_o_ext.split('.',1)
        username = s[0]
        repo_name = s[1]
        url = 'https://github.com/{0}/{1}'.format(username, repo_name)
        
        with open(target_readme_file_dir + filename, 'r', encoding='utf-8', errors='backslashreplace') as f:
            logging.info("Searching for candidate headings in file {0}".format(filename))
            content = f.read()
            # Perform abstraction on code section only before checking for potential headings
            # This is to reduce possibility of code snippets starting with '#' being read as potential headings
            # without changing genuine heading that happens to contain numbers or other things, e.g. '# Section 1'
            content2 = abstract_out_code_section(content)
            content_lines = content2.splitlines()
            
            # Start at first nonempty line index
            curr_filename_line_number = next(i for i, j in enumerate(content_lines) if j)
            
            section_id = 1
            while (curr_filename_line_number<len(content_lines)):
                found_candidate_heading = False
                line = content_lines[curr_filename_line_number]
                
                if line.startswith('#'):
                    heading_level = len(re.search('^#+', line).group(0))
                    heading_markdown = line
                    found_candidate_heading = True
                elif ((curr_filename_line_number<(len(content_lines)-1)) 
                    and (content_lines[curr_filename_line_number+1].startswith('---'))):
                    # H2 in underline markdown style
                    heading_level = 2
                    heading_markdown = '## ' + line
                    found_candidate_heading = True                    
                    # Skip next line (i.e. the underline)
                    curr_filename_line_number = curr_filename_line_number + 1                     
                elif ((curr_filename_line_number<(len(content_lines)-1)) 
                    and (content_lines[curr_filename_line_number+1].startswith('==='))):
                    # H1 in underline markdown style
                    heading_level = 1
                    heading_markdown = '# ' + line
                    found_candidate_heading = True
                    # Skip next line (i.e. the underline)
                    curr_filename_line_number = curr_filename_line_number + 1
                
                curr_filename_line_number = curr_filename_line_number + 1
                    
                # If heading is found
                if found_candidate_heading:
                    logging.info("Found candidate heading: {0}".format(line))
                    heading_text = extract_text_in_heading_markdown(heading_markdown)
                    abstracted_heading_markdown = abstract_text(heading_markdown).replace('\n', ' ').strip()
                    abstracted_heading_text = extract_text_in_heading_markdown(abstracted_heading_markdown)
                    
                    overview = overview.append({'section_id':section_id, 'file_id':file_id, 'url':url, 'local_readme_file':filename, 
                                        'heading_markdown':heading_markdown,
                                  'abstracted_heading_markdown':abstracted_heading_markdown, 'heading_text':heading_text, 
                                  'abstracted_heading_text':abstracted_heading_text,
                                  'heading_level':heading_level}, ignore_index=True)
                     
                    section_id = section_id + 1               
        file_id = file_id + 1
        
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
                    
    