# Voice-to-Text Note Taker 🎤

This is a simple Voice-to-Text Web Application built with Flask and Python's SpeechRecognition library.
It listens to your speech through the microphone, converts it into text, and displays the recognized sentences in a list on the webpage.

## 🚀 Features

🎙 Speech Recognition using Google's Speech API

📃 Real-time transcription displayed on the webpage

⏳ Shows when the app is listening

🎨 Styled with CSS for a clean UI

🖼 Mic icon as a favicon in the browser tab


## 📦 Dependencies

You need the following Python packages: <br>

**pip install flask** <br>
**pip install SpeechRecognition** <br>
**pip install pyttsx3** <br>
**pip install pyaudio** <br>

## Project Structure

voice-to-text/
│
├── static/ <br>
│   ├── styles.css          # CSS styling <br>
│   ├── mic_icon.png        # Mic logo for favicon <br>
│
├── templates/ <br>
│   ├── index.html          # Web UI <br>
│
├── app.py                  # Flask backend <br>
├── README.md               # Documentation <br>

## Usage
- Click the Start Listening button on the web page.

- Speak clearly into your microphone.

- Your recognized speech will appear in a list.

- If the system cannot understand, it will display  ....

## 🖼 Example Screenshot <br>

<img width="550" height="550" alt="image" src="https://github.com/user-attachments/assets/30cdcf57-f383-4729-8e44-82b8262043e9" />

## 📜 License

- This project is open-source under the MIT License.
