import configparser
import sys
import sqlite3
import logging

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../../config/config.cfg')
    db_filename = config['DEFAULT']['db_filename']
    log_filename = '../../log/empty_all_tables.log'
    
    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    try:
        logging.info('Emptying all tables')
        conn = sqlite3.connect(db_filename)
        # Delete existing data
        c = conn.cursor()
        c.execute('DELETE FROM section_overview_25pct')
        c.execute('DELETE FROM section_content_25pct')
        c.execute('DELETE FROM section_overview_75pct')
        c.execute('DELETE FROM section_content_75pct')
        c.execute('DELETE FROM section_content_combined')
        c.execute('DELETE FROM section_overview_combined')
        c.execute('DELETE FROM target_section_overview')
        c.execute('DELETE FROM target_section_content')
        conn.commit()
        logging.info('Operation completed')
    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()