from flask import Flask
app = Flask(__name__)

@app.route("/Desktop/Code!/borderify/hellp.py")
def hello():
    print ("Hello World!")

