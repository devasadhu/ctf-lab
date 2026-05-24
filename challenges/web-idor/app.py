from flask import Flask, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "notsecret"

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            bio TEXT
        )
    """)
    c.executemany("INSERT INTO users VALUES (?,?,?,?)", [
        (1, "admin", "supersecret", "CTF{idor_means_trust_no_client_input}"),
        (2, "alice", "password1", "Just a regular user."),
        (3, "guest", "guest",     "Guest account. Nothing to see here."),
    ])
    conn.commit()
    return conn

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("profile", id=user["id"]))
        return "Invalid credentials", 401
    return """
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    """

@app.route("/user")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = request.args.get("id")
    if int(user_id) != session["user_id"]:
        return "Forbidden", 403
    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE id=?", (user_id,)
    ).fetchone()
    if not user:
        return "User not found", 404
    return f"""
        <h2>Profile</h2>
        <p>Username: {user['username']}</p>
        <p>Bio: {user['bio']}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
