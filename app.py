from flask import Flask, render_template, jsonify
import speech_recognition as sr
import time

app = Flask(__name__)
r = sr.Recognizer()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listen", methods=["GET"])
def listen():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)  # faster ambient adjustment
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  # limits time

            text = r.recognize_google(audio)
            return jsonify({"status": "success", "text": text})

    except sr.WaitTimeoutError:
        return jsonify({"status": "error", "text": "No speech detected."})
    except sr.UnknownValueError:
        return jsonify({"status": "error", "text": "Could not understand audio."})
    except sr.RequestError as e:
        return jsonify({"status": "error", "text": f"Request error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
