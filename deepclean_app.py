from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/result", methods=["GET", "POST"])
def christmas_story():

    return render_template("result.html")

