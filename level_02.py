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

    
if __name__ == "__main__":
    app.run(debug=True)