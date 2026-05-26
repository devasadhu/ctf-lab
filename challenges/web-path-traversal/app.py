from flask import Flask, request
import os

app = Flask(__name__)
BASE_DIR = os.path.join(os.path.dirname(__file__), "files")

@app.route("/files")
def serve_file():
    filename = request.args.get("name")
    if not filename:
        return "No filename provided", 400

    filepath = os.path.realpath(os.path.join(BASE_DIR, filename))

    # Check the resolved path is still inside BASE_DIR
    if not filepath.startswith(BASE_DIR):
        return "Access denied", 403

    if not os.path.exists(filepath):
        return "File not found", 404

    with open(filepath, "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
