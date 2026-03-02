from flask import Flask, render_template, jsonify, request, session, redirect, url_for
import os

# Task 09: Session-Based Login System
"""
This will teach me:
1. How to use session in Flask
2. How to store login state
3. How to protect routes
4. How to log out

## What I'll implement:
1. GET /login → show login page (HTML form)
2. POST /login → verify username/password
3. If valid → store user in session
4. GET /dashboard → only accessible when logged in
5. GET /logout → destroy session and redirect to login
"""

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def default_route():
    return "This is Default Route: available routes are: ['/login', etc]"

# login route
@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["username"] = username
            return redirect(url_for('dashboard'))

        else:
            return "Invalid Credentials!"

# Assign dashboard to the logged-in users and maintain a session for that user
@app.route("/dashboard")
def dashboard():
    if session.get('username'):
        return f"Logged in as {session['username']}"
    else:
        return redirect(url_for('login'))

# Logout the user and clear the user from session and redirect the user to /login page
@app.route("/logout")
def logout():
    if session.get("username") is not None:
        session.pop('username', None)
        return redirect(url_for('login'))
    else:
        return f"Please login first"

if __name__ == "__main__":
    app.run(debug = True)