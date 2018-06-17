import logging
from script.helper.helper2 import *
import sqlite3
from sqlite3 import Error
import pandas
from pandas import DataFrame
import os

def abstract_out_markdown(filenames, readme_file_dir, temp_abstracted_markdown_file_dir):                 
    for f_row in filenames:
        filename = f_row[0]
        
        readme_file_full_path = readme_file_dir + filename
        # temp_html_file_full_path = temp_abstracted_html_file_dir + filename + '.html'
        temp_markdown_file_full_path = temp_abstracted_markdown_file_dir + filename
        logging.info('Processing {0}'.format(readme_file_full_path))
        # with open(readme_file_full_path, 'r', encoding='utf-8') as f:
        # use 'backslashreplace' to deal with UnicodeDecodeError
        with open(readme_file_full_path, 'r', encoding='utf-8', errors='backslashreplace') as f:
            text_with_markdown = f.read()  
            
            abstracted_markdown_text = abstract_text(text_with_markdown)
            
            # Write abstracted markdown to temp markdown directory
            with open(temp_markdown_file_full_path,'w',encoding='utf-8') as f_out_markdown:
                f_out_markdown.write(abstracted_markdown_text)
                
    logging.info("Abstraction of README file into temporary directory has been completed")

'''
Known issue: Unable to handle underline-style H1 and H2
'''
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
    
'''
Updated section extractor. Checks for underline-style H1 and H2
'''
def extract_section_from_abstracted_files_v2(temp_abstracted_markdown_file_dir, db_filename, overview_table, content_table):
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

'''
Extracts headings from unprocessed README files in a specified directory. 
To reduce false positives (lines starting with # that isn't actually a heading, such as comment lines in code snippets), 
abstract out code section blocks.
Perform no other abstraction to allow headings such as "Section 2", "Section 3", etc. to be extracted as is 
for later reference / manual checking (instead of having everything turned into "Section @abstr_number").
'''
def extract_headings_from_files_in_directory(target_readme_file_dir):
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
    return overview    