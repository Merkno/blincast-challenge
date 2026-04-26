from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DB_FILE = "database.json"


def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


@app.route("/document", methods=["POST"])
def document():
    data = request.json

    if not data:
        return jsonify({"status": "error", "code": 4})

    action = data.get("action")
    key = data.get("key")
    value = data.get("value")

    db = load_data()

    if action == "create":
        if key in db:
            return jsonify({"status": "error", "code": 1})
        db[key] = value
        save_data(db)

    elif action == "update":
        if key not in db:
            return jsonify({"status": "error", "code": 2})
        db[key] = value
        save_data(db)

    elif action == "delete":
        if key not in db:
            return jsonify({"status": "error", "code": 2})
        del db[key]
        save_data(db)

    else:
        return jsonify({"status": "error", "code": 3})

    return jsonify({"status": "ok", "code": 0})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)