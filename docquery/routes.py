from flask import Flask, render_template, url_for
from docquery import app

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("index.html")
