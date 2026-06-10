import sqlite3

def get_db():
    conn = sqlite3.connect('backend/music_heritage.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS music (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            genre TEXT NOT NULL,
            region TEXT NOT NULL,
            year INTEGER,
            description TEXT,
            video_url TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == '__main__':
    init_db()