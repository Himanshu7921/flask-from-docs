# Task 12 — Upload an Image (File Upload API)

import os
from flask import Flask, render_template, jsonify, request, send_file

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.pdf', 'jpeg']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok = True)


uploaded_files = []

@app.route("/upload", methods = ["POST", "GET"])
def upload():
    global UPLOAD_FOLDER
    if request.method == "GET":
        return render_template("upload.html")
    if request.method == "POST":
        uploaded_file = request.files['file']
        _, ext = os.path.splitext(uploaded_file.filename)
        if ext.lower() not in app.config['UPLOAD_EXTENSIONS']:
            return jsonify({"error": "Invalid file type"})
        
        if uploaded_file.filename != '':
            uploaded_files.append(str(uploaded_file.filename))
            upload_pth = f"{UPLOAD_FOLDER}/{uploaded_file.filename}"
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

# Task 13: Download a file
@app.route("/get_file_list", methods = ["GET"])
def get_list():
    global UPLOAD_FOLDER
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({
        "uploaded_files": files
    })

@app.route("/download/<file_name>")
def downoad_file(file_name: str):
    global UPLOAD_FOLDER
    path = f"{UPLOAD_FOLDER}/{file_name}"
    return send_file(path, as_attachment = True, download_name = file_name)

if __name__ == "__main__":
    app.run(debug=True)