import sqlite3
DB_NAME = 'database.db'

def initdb():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                visit_count INTEGER DEFAULT 0
            )                           
        ''')
        
def insert_url(original_url,short_code):
    with sqlite3.connect(DB_NAME) as conn:
     conn.execute('''
            INSERT INTO urls (original_url,short_code) VALUES(?,?)
                                       
        ''',(original_url,short_code))
    
def get_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
            SELECT * FROM urls WHERE short_code = ?             
        ''',(short_code,)) # put comma 
        return cur.fetchone()    
    
def incerement_visit_count(short_code):
     with sqlite3.connect(DB_NAME) as conn:
         conn.execute('''
        UPDATE urls 
        SET visit_count = visit_count + 1
        WHERE short_code = ?              
        ''',(short_code,))
    
def get_all_urls():
    with sqlite3.connect(DB_NAME) as conn:
        curr = conn.execute('SELECT original_url, short_code, visit_count FROM urls ORDER BY id DESC')
        return curr.fetchall()
    
def delete_url_by_code(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE from urls WHERE short_code = ?',(short_code,))         
    
    
    