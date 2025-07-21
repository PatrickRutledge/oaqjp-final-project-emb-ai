"""Flask web app for emotion detection"""

import requests
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Renders the main index page with input form."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyzes emotions from the input text.

    Returns:
        str: HTML-formatted emotion scores and dominant emotion,
             or error message if analysis fails.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    try:
        response = emotion_detector(text_to_analyze)
    except ValueError as error:
        return f"Invalid input: {str(error)}"
    except requests.exceptions.RequestException as error:
        return f"Request failed: {str(error)}"

    if not response or response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")
    dominant_emotion = response.get("dominant_emotion")

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
