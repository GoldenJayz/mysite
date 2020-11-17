from flask import Flask
from flask import render_template
from flask import request
from flask import *

app = Flask(__name__)

@app.route("/home")
def home():
  return render_template("index.html")

@app.route("/")
def homee():
  return render_template("index.html")

@app.route("/github")
def github():
  return redirect("https://github.com/GoldenJayz")

@app.route("/puck")
def puck():
  return redirect("https://puckpanel.glitch.me/")

@app.route("/about")
def about():
  return render_template("about.html")


if __name__ == "__main__":
  app.run()