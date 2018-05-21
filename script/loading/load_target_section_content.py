import configparser
import logging
import sqlite3
from sqlite3 import Error
from script.helper.helper2 import *
import sys
import os
import shutil
import pandas

def abstract_out_markdown(filenames):                 
    for f_row in filenames:
        filename = f_row[0]
        
        readme_file_full_path = readme_file_dir + filename
        # temp_html_file_full_path = temp_abstracted_html_file_dir + filename + '.html'
        temp_markdown_file_full_path = temp_abstracted_markdown_file_dir + filename
        logging.info('Processing {0}'.format(readme_file_full_path))
        
        with open(readme_file_full_path, 'r', encoding='utf-8', errors='backslashreplace') as f:
            text_with_markdown = f.read()  
            
            abstracted_markdown_text = abstract_text(text_with_markdown)
            
            # Write abstracted markdown to temp markdown directory
            with open(temp_markdown_file_full_path,'w',encoding='utf-8') as f_out_markdown:
                f_out_markdown.write(abstracted_markdown_text)
                
    logging.info("Abstraction of README file into temporary directory has been completed")

def extract_section_from_abstracted_files(temp_abstracted_markdown_file_dir):
    conn = sqlite3.connect(db_filename)
    try:
        c = conn.cursor()
        logging.info("Fetching information of section to extract and load")
        
        headings = pandas.read_sql("""
            SELECT file_id, section_id, local_readme_file, heading_markdown, abstracted_heading_markdown, heading_text, NULL as content_text_w_o_tags
            FROM target_section_overview 
            ORDER BY file_id, section_id""", conn)
        
        curr_filename = None
        curr_filename_lines = None
        curr_filename_line_number = 0
        # Section definition: lines between current heading and next, regardless of level
        # Can't simply use equivalent of left JOIN between list of headings and actual headings in file,
        # as a file may have a several heading with same text and level (e.g. multiple "Example" subheadings, one for each method in a reference section)
        for i,r in headings.iterrows():
            heading_already_found = False
            
            local_readme_filename = r[2]
            heading_markdown = r[3]
            abstracted_heading_markdown = r[4]
            logging.info('Searching for abstracted heading: {0}'.format(abstracted_heading_markdown))
            heading_text = r[5]
            if (curr_filename is None) or (curr_filename != local_readme_filename):
                curr_filename = local_readme_filename
                logging.info('Reading {0}'.format(temp_abstracted_markdown_file_dir + curr_filename))
                with open (temp_abstracted_markdown_file_dir + curr_filename, "r", encoding='utf-8', errors='backslashreplace') as myfile:
                    # Read as is, use rstrip instead of strip to only remove trailing whitespace
                    # We want to preserve leading whitespace to avoid treating line starting with space/tab followed by #
                    # from being treated as heading
                    curr_filename_lines = myfile.readlines()                    
                    curr_filename_lines = [x.rstrip() for x in curr_filename_lines]
                curr_filename_line_number = 0                
            
            curr_section_content_lines = []
            # Iterate through file until heading markdown is found or end of file is found
            # Check also for underline-style formatting
            while (curr_filename_line_number<len(curr_filename_lines)):
                '''
                If a candidate heading is found, compare it with the heading we're looking for.
                If it's actually the one we want, set a flag, so if the next heading happens to have same string,
                we can tell that it's a different heading.
                There may be case where the heading in DB
                '''
                if curr_filename_lines[curr_filename_line_number].startswith('#'):
                    # Potential heading, starting with #. Is it the heading we want?
                    candidate_heading = curr_filename_lines[curr_filename_line_number].replace('\n',' ').strip() 
                    if ((candidate_heading != abstracted_heading_markdown.strip()) or heading_already_found):
                        logging.info('Encountered new heading in document: {0}'.format(candidate_heading))
                        break
                    else:
                        logging.info('Found the heading for {0}'.format(heading_markdown))
                        heading_already_found = True
                elif ((curr_filename_line_number<len(curr_filename_lines)-1) and
                     curr_filename_lines[curr_filename_line_number+1].startswith('===')):
                    # Potential H1, in underline markdown style
                    candidate_heading = curr_filename_lines[curr_filename_line_number].replace('\n',' ').strip() 
                    if (('# ' + candidate_heading) != abstracted_heading_markdown.strip() or heading_already_found):
                        logging.info('Encountered candidate underline-style H1 in document: {0}'.format(candidate_heading))
                        # Skip next line (which is the underline)
                        curr_filename_line_number += 1                        
                        break
                    else:
                        logging.info('Found the heading for {0}'.format(heading_markdown)) 
                        heading_already_found = True
                elif ((curr_filename_line_number<len(curr_filename_lines)-1) and 
                     curr_filename_lines[curr_filename_line_number+1].startswith('---')):
                    # Potential H2, in underline markdown style
                    candidate_heading = curr_filename_lines[curr_filename_line_number].replace('\n',' ').strip() 
                    if (('## ' + candidate_heading) != abstracted_heading_markdown.strip() or heading_already_found):
                        logging.info('Encountered candidate underline-style H2 in document: {0}'.format(candidate_heading))
                        # Skip next line (which is the underline)
                        curr_filename_line_number += 1                        
                        break
                    else:
                        logging.info('Found the heading for {0}'.format(heading_markdown))
                        heading_already_found = True
                else:
                    curr_section_content_lines.append(curr_filename_lines[curr_filename_line_number])
                
                # Proceed to next line
                curr_filename_line_number += 1
            
            curr_section_content = ' '.join(curr_section_content_lines)
            curr_section_content_w_o_tags = extract_text_from_markdown_snippet(curr_section_content)
            headings.set_value(i,'content_text_w_o_tags',curr_section_content_w_o_tags)
        
        df_to_save = headings[['file_id','section_id','content_text_w_o_tags']]
        # Use append when saving since table is already emptied at the beginning
        df_to_save.to_sql(name='target_section_content', con=conn, if_exists='append', index=False)
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()
        
    logging.info("Loading of section contents has been completed")
    
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    readme_file_dir = config['DEFAULT']['target_readme_file_dir']
    temp_abstracted_markdown_file_dir = config['DEFAULT']['temp_target_abstracted_markdown_file_dir']
    
    log_filename = '../../log/load_target_section_content.log'
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    conn = sqlite3.connect(db_filename)
    try:
        c = conn.cursor()
        logging.info("Cleaning existing data")
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
        
    abstract_out_markdown(filenames)
    extract_section_from_abstracted_files(temp_abstracted_markdown_file_dir)