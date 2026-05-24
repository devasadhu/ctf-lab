import sqlite3
import os
from flask import Flask, request, render_template_string

app = Flask(__name__)
DATABASE = 'ctf.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS secrets (
        id INTEGER PRIMARY KEY,
        flag TEXT
    )''')
    c.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'supersecretpassword')")
    c.execute("INSERT OR IGNORE INTO users VALUES (2, 'guest', 'guest123')")
    c.execute("INSERT OR IGNORE INTO secrets VALUES (1, 'CTF{blind_sqli_is_all_about_asking_yes_or_no}')")
    conn.commit()
    conn.close()

LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>CorpNet Login</title></head>
<body>
    <h2>CorpNet Employee Portal</h2>
    <form method="POST" action="/login">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>
        <label>Password:</label><br>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    conn = get_db()
    c = conn.cursor()

    query = "SELECT * FROM users WHERE username=?"

    try:
        c.execute(query, (username,))
        user = c.fetchone()
    except:
        user = None
    finally:
        conn.close()

    if user:
        return render_template_string(LOGIN_PAGE, message="Welcome back!")
    else:
        return render_template_string(LOGIN_PAGE, message="Invalid credentials.")

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
