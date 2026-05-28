from flask import Flask, request, jsonify, session
import time

app = Flask(__name__)
app.secret_key = "supersecret"

# Each user starts with 1 token
balances = {"alice": 1}
flag = "CTF{race_conditions_break_atomicity}"

@app.route("/balance")
def balance():
    user = request.args.get("user", "alice")
    return jsonify({"user": user, "balance": balances.get(user, 0)})

@app.route("/redeem")
def redeem():
    user = request.args.get("user", "alice")

    # STEP 1 — CHECK
    if balances.get(user, 0) < 1:
        return jsonify({"error": "not enough tokens"}), 403

    # Artificial delay between check and use — simulates real processing time
    time.sleep(0.1)

    # STEP 2 — USE
    balances[user] -= 1
    return jsonify({"result": "redeemed!", "flag": flag})

@app.route("/reset")
def reset():
    balances["alice"] = 1
    return jsonify({"reset": True})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
