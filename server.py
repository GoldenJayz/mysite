from flask import Flask
from flask import render_template
from flask import request
from flask import *
import os
import json

app = Flask(__name__)


@app.route("/home")
def home():
  return render_template("puckdata.html")

@app.route("/")
def homee():
  return render_template("puckdata.html")

@app.route("/github")
def github():
  return redirect("https://github.com/GoldenJayz")

@app.route("/puck")
def puck():
  return redirect("https://puckpanel.glitch.me/")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/html")
def html():
  return render_template("puckdata.html")

@app.route("/home/puck")
def phuck():
  return redirect("https://github.com/GoldenJayz/puck")

@app.route("/home/logs")
def logs():
  return render_template("logs.html")

@app.route("/home/music")
def music():
  return redirect("https://github.com/GoldenJayz/puck2")


if __name__ == "__main__":
  app.run()
