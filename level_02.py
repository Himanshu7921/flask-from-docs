# GET method for /login and take user_name and pass as an HTML form
# POST method for /login and verify the user_name and pass


from flask import Flask, request, jsonify, render_template, make_response


app = Flask(__name__)

@app.route("/")
def checking():
    return "Okay"

# Task-04: Handling GET and POST with HTML Form and validating requests using 'request.method'
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "1234":
            return "Login Sucessfull"
        else:
            return "Invalid Credentials"


# Task-05: POST Requests Handling with request.get_json(..) and return json with jsonify({...})
@app.route("/validate", methods = ["POST"])
def analyze():
    data = request.get_json()
    num = data.get("number")
    if num is not None:
        if num > 0:
            sign = "Positive"
        else:
            sign = "Negative"
        
        if num % 2 == 0:
            even_or_odd = "Even"

        elif num % 2 != 0:
            even_or_odd = "Odd"
        
        return jsonify({
            "number": num,
            "even_or_odd": even_or_odd,
            "sign": sign
        })
    
    else:
        return "Number is None"

   
# Task-06: Temperature Converter API
@app.route("/convert-temp", methods = ["POST"])
def convert_temp():
    data = request.get_json()
    temp = int(data.get("temperature"))
    scale = data.get("scale")
    input_temp = str(temp) + scale
    if scale == "F":
        convert_temp = str((temp - 32) * (5/9)) + str(" C")
    elif scale == "C":
        convert_temp = str(((9/5) * temp) + 32) + str(" F")
    else:
        return "Scale must be ['F' or 'C'] nothing else"
    
    return jsonify({
        "input": input_temp,
        "converted_to": convert_temp
    })


# Task-07: Basic Calculator API
@app.route("/calc", methods = ["POST"])
def calculator():
    data = request.get_json()
    a = int(data.get("a"))
    b = int(data.get("b"))
    c = data.get("op")
    if c == "+":
        result = a + b
    elif c == "/":
        if b != 0:
            result = a / b
        else:
            result = "Division by zero is not possible"
    elif c == "-":
        result = a - b
    elif c == "*":
        result = a * b
    else:
        return "Enter a valid operator from ['+', '-', '*', '/']"
    expression = str(a) + str(c) + str(b)
    return jsonify({
        "input": expression,
        "result": result
    })

# Task 08: Cookie-Based Visitor Counter
"""
cookies are read using the request.cookies.get() method and set using the response.set_cookie() method.
Cookies are a way to store data on the client's browser to persist information between stateless HTTP requests.

Tips for Working with Cookies in Flask

1. Always return a Flask Response object — cookies can only be attached to responses.
2. The browser updates its cookies only when the server returns a Response object that contains the Set-Cookie header.
3. Wrap your output (JSON/text/HTML) using make_response(), get the response object, set the cookie on it, and return that response.
"""
@app.route("/visitor", methods = ["GET"])
def visitor():
    count = int(request.cookies.get("visitor_count", default = 0))
    count += 1
    if count == 1:
        disply_message = "Hello first-time visitor!"
    elif count > 1:
        disply_message = "Welcome back!"
    
    data = jsonify({
        "message": disply_message,
        "visits": str(count)
    })

    response = make_response(data)
    response.set_cookie("visitor_count", str(count))

    return data

if __name__ == "__main__":
    app.run(debug=True)