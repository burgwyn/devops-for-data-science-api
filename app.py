import os
from flask import Flask, Request, Response, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/hello")
def hello():
    return Response('{ "message": "Hello World!" }', mimetype="application/json")

@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return Response('{ "message": "No file part" }', mimetype="application/json")
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return Response('{ "message": "No selected file" }', mimetype="application/json")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return Response('{ "message": "File saved" }', mimetype="application/json")
    return Response('{ "message": "Error" }', mimetype="application/json")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)