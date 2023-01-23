from flask import Flask, render_template, request

import random

app = Flask(__name__)

secret = 25

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess/", methods=["GET"])
def guess():
    
    return render_template("guess.html", numbers = range(101))

@app.route("/response/<int:guess>", methods=["GET"])
def response(guess):
    secret = 25
    return render_template("response.html", guess=guess, secret=secret)



