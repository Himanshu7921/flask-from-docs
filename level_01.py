from flask import Flask, render_template, jsonify, request
from markupsafe import escape
import math


app = Flask(__name__)


# Task-01

# Define Routes
@app.route("/", methods = ["GET"]) # Default Route
def default_route():
    return render_template("index.html")

@app.route("/contact")
def contact_route():
    return render_template("contact.html")


@app.route("/home")
def home_route():
    return render_template("home.html")

@app.route("/about")
def about_route():
    return render_template("about.html")

# Task-02: Passing parameters in URL Routes
@app.route("/hello/<name>")
def say_hello(name: str):
    return f"Hello, {name}"

@app.route("/square/<int:num>")
def square_num(num: int):
    return f"{num ** 2}"


if __name__ == "__main__":
    app.run(debug=True)

