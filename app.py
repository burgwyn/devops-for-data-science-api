from flask import Flask, Request, Response
app = Flask(__name__)

@app.route("/hello")
def hello():
    return Response('{ "message": "Hello World!" }', mimetype="application/json") 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)