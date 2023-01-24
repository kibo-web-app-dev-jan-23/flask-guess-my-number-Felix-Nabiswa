from flask import Flask, render_template, request

import random

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game/", methods=["GET"])
def game():
    return render_template("game.html", numbers = range(101))

@app.route("/guess/<int:guess>", methods=["GET"])
def guess(guess):
    return render_template("guess.html", guess=guess, secret_number=secret_number)


