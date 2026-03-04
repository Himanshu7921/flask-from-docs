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


if __name__ == "__main__":
    app.run(debug = False)