from flask import Flask,render_template 
app=Flask(__name__)

@app.route("/")
def fristclass():
    return "thisis my frist class progarm "


@app.route("/index")
def frist_webpage():
    return render_template("index.html")
app.run(debug=True)