from flask import Flask 
app=Flask(__name__)

@app.route("/")
def fristclass():
    return "thisis my frist class progarm "

@app.route("/flask2")
def secondclass():
    return "python is fun"
app.run()