# Task 12 — Upload an Image (File Upload API)

import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.pdf', 'jpeg']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok = True)

@app.route("/upload", methods = ["POST", "GET"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    if request.method == "POST":
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            upload_pth = f"uploads/{uploaded_file.filename}"
            uploaded_file.save(upload_pth)        
            return jsonify({
                "message": "File uploaded successfully",
                "filename": str(uploaded_file.filename),
                "saved_to": str(upload_pth)
            })
        else:
            return jsonify({
                "error": "Please upload the file"
            })


if __name__ == "__main__":
    app.run(debug=True)