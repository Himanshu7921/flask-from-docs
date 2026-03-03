# Task 11: Build a URL shortener
from flask import Flask, redirect, jsonify, request
import string, random

app = Flask(__name__)


# Global mapping dict
mapping = dict()

@app.route("/")
def default_route():
    return "This is default route, available routes: ['POST /shorten ', 'GET /shorten_code']"

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/shorten", methods = ["POST"])
def shorten_url():
    global mapping

    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({
            "error": "url field is required", 
        }), 404
    else:
        short_code = generate_code()
        mapping[short_code] = url
        return jsonify({
            "actual_url": str(url),
            "shorten_url": f"http://127.0.0.1:5000/{short_code}"
        })
        

@app.route("/shorten/<short_code>", methods = ["GET"])
def get_actual_url(short_code: str):
    global mapping
    if short_code not in mapping:
        return jsonify({
            "error": "The url dsn't exist in our database"
        })
    else:
        return redirect(mapping[short_code])


if __name__ == "__main__":
    app.run(debug = True)