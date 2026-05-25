from flask import Flask, request, jsonify
import jwt
import sqlite3

app = Flask(__name__)
SECRET_KEY = "supersecretkey123"
FLAG = "CTF{jwt_none_algorithm_is_a_lie}"

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, role TEXT)")
    c.execute("DELETE FROM users")
    c.execute("INSERT INTO users VALUES (1, 'admin', 'admin')")
    c.execute("INSERT INTO users VALUES (2, 'guest', 'user')")
    conn.commit()
    conn.close()

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT role FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()

    if not row:
        return jsonify({"error": "User not found"}), 401

    role = row[0]
    token = jwt.encode({"username": username, "role": role}, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})

@app.route("/admin")
def admin():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if decoded.get("role") == "admin":
            return jsonify({"message": "Welcome admin!", "flag": FLAG})
        else:
            return jsonify({"error": "Access denied"}), 403
    except Exception as e:
        return jsonify({"error": str(e)}), 401

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
