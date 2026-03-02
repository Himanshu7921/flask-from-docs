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


# Task=03: Query Parameters
@app.route("/query")
def get_name():
    name = request.args.get("name")
    age = request.args.get("age")
    occupation = request.args.get("occupation")
    if name is not None and age is not None and occupation is not None:
        return jsonify({
            "name": name,
            "age": age,
            "occupation": occupation
        })
    else:
        return "Pass Query as name, age and occupation in URL"

@app.route("/calc")
def calculator():
    num = int(request.args.get("num"))
    op = request.args.get("op")
    
    if num is None:
        return "Please pass number as Query as ('?num=10')"
    
    if op is None:
        return "Please pass op as Query as ('?op=operator'), available operators = ['cube', 'square', 'sqrt']"
    
    if op == "sqrt":
        return f"sqrt({num}) = {math.sqrt(num)}"
    elif op == "square":
        return f"square({num}) = {math.pow(num, 2)}"
    elif op == "cube":
        return f"cube({num}) = {math.pow(num, 3)}"

if __name__ == "__main__":
    app.run(debug=True)

