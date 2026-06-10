import sys
sys.path.insert(0, 'backend')

from flask import Flask, render_template
from database import get_db

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM music')
    music_list = cursor.fetchall()
    conn.close()
    return render_template('index.html', music_list=music_list)

@app.route('/browse')
def browse():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM music')
    music_list = cursor.fetchall()
    conn.close()
    return render_template('browse.html', music_list=music_list)

if __name__ == '__main__':
    app.run(debug=True)