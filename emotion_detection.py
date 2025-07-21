import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion in the given text using Watson NLP Emotion Detection service.
    
    Args:
        text_to_analyse (str): The text to analyze for emotions
        
    Returns:
        dict: The response from the emotion detection service
    """
    # Define the URL for the Watson NLP Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers with the required model ID
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Create the input JSON with the text to analyze
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    try:
        # Make the POST request to the Watson NLP service
        response = requests.post(url, json=input_json, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            response_data = response.json()
            return response_data
        else:
            return {"error": f"Request failed with status code: {response.status_code}"}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}