from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    k = ["kot", "piesek","aligator"]
    return render_template("index.html", k = k)



@app.route("/test")
def another_hello():
    return "<p>Hello Fortnite!</p>"