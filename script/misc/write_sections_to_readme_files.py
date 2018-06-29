'''
Writes processed 'what' and 'why' sections to files with same names as original README files
'''
import configparser
import logging
import sqlite3
import pandas
from sqlite3 import Error
import time
import os        

if __name__ == '__main__':
    start = time.time()
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    dirname = "../../output/readmes"
    log_filename = '../../log/write_sections_to_readme_files.log'
    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    conn = sqlite3.connect(db_filename)
    try:
        sql_text = """
        SELECT t1.local_readme_file, t1.abstracted_heading_text, t2.content_text_w_o_tags
        FROM target_section_overview t1 JOIN target_section_content t2
        ON t1.file_id = t2.file_id AND t1.section_id = t2.section_id
        WHERE instr(section_code,'1')
        ORDER BY t1.file_id, t1.section_id
        """
        df = pandas.read_sql_query(con=conn, sql=sql_text)
        prev_readme_name = ""
        f = None
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        for index, row in df.iterrows():
            cur_readme_name = row['local_readme_file']
            if prev_readme_name != cur_readme_name: 
                if f:
                    f.close()
                prev_readme_name = cur_readme_name
                f=open(dirname +"/" + cur_readme_name,'wb')
                logging.info('Writing {0}'.format(cur_readme_name))
            f.write(row['abstracted_heading_text'].encode('utf-8')+'\n'.encode('utf-8'))
            f.write(row['content_text_w_o_tags'].encode('utf-8')+'\n'.encode('utf-8'))
        f.close()
        
        end = time.time()
        runtime_in_seconds = end - start
        logging.info('Processing completed in {0}'.format(runtime_in_seconds))
    except Error as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()