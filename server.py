from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the main index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    try:
        response = emotion_detector(text_to_analyze)
    except Exception as e:
        return f"Error in emotion detection: {str(e)}"

    # Check for missing or invalid keys
    if not response or response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

    return formatted_response


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)