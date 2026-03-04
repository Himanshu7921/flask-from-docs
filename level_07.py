from flask import Flask, request, jsonify

app = Flask(__name__)


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


@app.route("/")
def default_route():
    return "This is default route"


if __name__ == "__main__":
    app.run(debug = False)