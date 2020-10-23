from flask import Flask
app = Flask(__name__) # flask var to instance 

@app.route("/")
def hello():
    return "Hello World"
