from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the main index page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze emotion from text input and return formatted response"""
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Check if text is provided
    if not text_to_analyze:
        return "No text provided for analysis"
    
    # Get the emotion analysis results
    response = emotion_detector(text_to_analyze)
    
    # Check for errors in the response
    if 'error' in response:
        return f"Error in emotion detection: {response['error']}"
    
    # Extract individual emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Format the response string as requested
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )
    
    return formatted_response

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)