from flask import Flask, render_template, jsonify
import speech_recognition as sr

app = Flask(__name__)
r = sr.Recognizer()

@app.route("/")
def index():
    return render_template("index.html")

