from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
FLAG = "CTF{ssrf_makes_the_server_your_proxy}"

@app.route("/internal/admin")
def internal_admin():
    if request.headers.get("X-Internal-Request") != "true":
        return jsonify({"error": "Access denied — internal only"}), 403
    return jsonify({"secret": FLAG})

@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Whitelist — only allow specific trusted domains
    allowed = ["example.com", "trusted-api.com"]
    if not any(domain in url for domain in allowed):
        return jsonify({"error": "Domain not allowed"}), 403

    try:
        response = requests.get(url, timeout=3, headers={"X-Internal-Request": "true"})
        return jsonify({"content": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
