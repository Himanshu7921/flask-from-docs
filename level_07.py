from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)


# Task-15: Custom error pages
@app.errorhandler(404)
def page_not_found(error): # If route dsn't exists then we get Error 404
    return """
    <html>
        <head>
            <title>404 - Page Not Found</title>
        </head>
        <body style="text-align:center;font-family:sans-serif">
            <h1>404</h1>
            <h2>Page Not Found</h2>
            <p>The page you are looking for does not exist.</p>
        </body>
    </html>
    """, 404

@app.errorhandler(500)
def server_error(error):
    return """
    <html>
        <head>
            <title>500 - Server Error</title>
        </head>
        <body style="text-align:center;font-family:sans-serif">
            <h1>500</h1>
            <h2>Internal Server Error</h2>
            <p>Something went wrong on the server.</p>
        </body>
    </html>
    """, 500

@app.route("/crash") # For Triggering Error-500, but set 'debug = False' for this
def crash():
    return str(1 / 0)

@app.route("/")
def default_route():
    return "This is default route"

# Task-16: Create a rate limiter
"""
A system that:
    1. Tracks requests per IP
    2. Stores request timestamps
    3. Allows maximum 5 requests in 60 seconds
    4. Blocks further requests

Example behavior:
    IP: 127.0.0.1
    Request 1 → allowed
    Request 2 → allowed
    Request 3 → allowed
    Request 4 → allowed
    Request 5 → allowed
    Request 6 → blocked (429 Too Many Requests)
"""

rate_limiter = dict()
TIME_LIMIT = 10.0
RATE_LIMIT = 5

def remove_older_timestamps(ip: str, older_time_in_sec: float):
    current_time = datetime.now()
    time_stamp_list = rate_limiter[ip]
    for t in time_stamp_list.copy():
        if (current_time - t).total_seconds() > int(older_time_in_sec):
            rate_limiter[ip].remove(t)

@app.before_request
def log_ip():
    global RATE_LIMIT
    global TIME_LIMIT
    ip = request.remote_addr
    timestamp = datetime.now()
    if ip not in rate_limiter:
        rate_limiter.setdefault(ip, [timestamp])
    else:
        remove_older_timestamps(ip, TIME_LIMIT)
        if len(rate_limiter[ip]) > RATE_LIMIT - 1:
            return jsonify({
                "RATE_LIMIT_ERROR": "You have reached maximum number of request per IP Address, try changing your IP Address by VPN"
            }), 429
        rate_limiter[ip].append(timestamp)
    print(rate_limiter)

@app.route("/hello")
def hello():
    return "Hello!"


if __name__ == "__main__":
    app.run(debug = True)