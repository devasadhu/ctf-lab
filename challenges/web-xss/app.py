from flask import Flask, request, session, render_template_string

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config["SESSION_COOKIE_HTTPONLY"] = False

messages = []

FLAG = "CTF{xss_steals_cookies_not_just_alerts}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        msg = request.form["message"]
        messages.append(msg)

    template = """
    <h2>Message Board</h2>
    <form method="POST">
        <input name="message" placeholder="Post a message">
        <button type="submit">Post</button>
    </form>
    <hr>
    {% for msg in messages %}
        <p>{{ msg | safe }}</p>
    {% endfor %}
    """
    return render_template_string(template, messages=messages)

@app.route("/admin")
def admin():
    session["flag"] = FLAG
    return f"Admin panel. Your session is set. <a href='/'>Go to board</a>"

if __name__ == "__main__":
    app.run(debug=True)
