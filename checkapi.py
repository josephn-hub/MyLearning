from flask import Flask
import requests
import jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return f"Hello World!"


@app.route('/get-request/<username>')
def get_request(username):
    user = {
        "username": username,
        "role_id": 123,
        "branch": "computer Science"
    }
    return jsonify(user), 200


if __name__ == '__main__':
    app.run(debug=True)
