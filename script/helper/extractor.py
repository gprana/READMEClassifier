import logging
from script.helper.helper2 import *
import sqlite3
from sqlite3 import Error
import pandas

def abstract_out_markdown(filenames, readme_file_dir, temp_abstracted_markdown_file_dir):                 
    for f_row in filenames:
        filename = f_row[0]
        
        readme_file_full_path = readme_file_dir + filename
        # temp_html_file_full_path = temp_abstracted_html_file_dir + filename + '.html'
        temp_markdown_file_full_path = temp_abstracted_markdown_file_dir + filename
        logging.info('Processing {0}'.format(readme_file_full_path))
        with open(readme_file_full_path, 'r', encoding='utf-8') as f:
            text_with_markdown = f.read()  
            
            abstracted_markdown_text = abstract_text(text_with_markdown)
            
            # Write abstracted markdown to temp markdown directory
            with open(temp_markdown_file_full_path,'w',encoding='utf-8') as f_out_markdown:
                f_out_markdown.write(abstracted_markdown_text)
                
    logging.info("Abstraction of README file into temporary directory has been completed")

def extract_section_from_abstracted_files(temp_abstracted_markdown_file_dir, db_filename, overview_table, content_table):
    conn = sqlite3.connect(db_filename)
    try:
        c = conn.cursor()
        logging.info("Fetching information of section to extract and load")
        
        headings = pandas.read_sql("""
            SELECT file_id, section_id, local_readme_file, heading_markdown, abstracted_heading_markdown, heading_text, NULL as content_text_w_o_tags
            FROM {0} 
            ORDER BY file_id, section_id""".format(overview_table), conn)
        
        curr_filename = None
        curr_filename_lines = None
        curr_filename_line_number = 0
        # Section definition: lines between current heading and next, regardless of level
        # Iterate through file sequentially since a file may have a several heading with same text and level 
        # (e.g. multiple "Example" subheadings, one for each method in a reference section)
        for i,r in headings.iterrows():
            local_readme_filename = r[2]
            heading_markdown = r[3]
            abstracted_heading_markdown = r[4]
            logging.info('Searching for abstracted heading: {0}'.format(abstracted_heading_markdown))
            heading_text = r[5]
            if (curr_filename is None) or (curr_filename != local_readme_filename):
                curr_filename = local_readme_filename
                logging.info('Reading {0}'.format(temp_abstracted_markdown_file_dir + curr_filename))
                with open (temp_abstracted_markdown_file_dir + curr_filename, "r", encoding='utf-8') as myfile:
                    # Read as is, use rstrip instead of strip to only remove trailing whitespace
                    # We want to preserve leading whitespace to avoid treating line starting with space/tab followed by #
                    # from being treated as heading
                    curr_filename_lines = myfile.readlines()                    
                    curr_filename_lines = [x.rstrip() for x in curr_filename_lines]
                curr_filename_line_number = 0                
            
            curr_section_content_lines = []
            # Iterate through file until heading markdown is found or end of file is found
            while (curr_filename_line_number<len(curr_filename_lines)):
                if curr_filename_lines[curr_filename_line_number].startswith('#'):
                    # Found a potential heading. Is it the heading we want?
                    # Replace any type of newline (that may not count as newline in current system) with space
                    candidate_heading = curr_filename_lines[curr_filename_line_number].replace('\n',' ').strip() 
                    # Perform comparison
                    if candidate_heading != abstracted_heading_markdown.strip():
                        # We've reached a new heading. The heading we wanted is not found.
                        # Possible with the case of a non-heading line starting with # being mislabeled as heading
                        logging.info('Encountered heading in document: {0}'.format(candidate_heading))
                        break
                    else:
                        logging.info('Found the heading for {0}'.format(heading_markdown))
                else:
                    curr_section_content_lines.append(curr_filename_lines[curr_filename_line_number])
                curr_filename_line_number += 1
            
            curr_section_content = ' '.join(curr_section_content_lines)
            curr_section_content_w_o_tags = extract_text_from_markdown_snippet(curr_section_content)
            # logging.debug('Content of {0}'.format(heading_markdown))
            # logging.debug(curr_section_content)
            # logging.debug('After markdown removal')
            # logging.debug(curr_section_content_w_o_tags)
            headings.set_value(i,'content_text_w_o_tags',curr_section_content_w_o_tags)
        
        df_to_save = headings[['file_id','section_id','content_text_w_o_tags']]
        # Use append when saving since table is already emptied at the beginning
        df_to_save.to_sql(name=content_table, con=conn, if_exists='append', index=False)
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()
        
    logging.info("Loading of section contents has been completed")