import requests
from decouple import config

ELEVEN_LABS_API_KEY = config('ELEVEN_LABS_API_KEY')

# Eleven Labs - text to speech
def convert_text_to_speech(message):
    # Define data body for request
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }
    
    # Define voice from 11 labs api websites list of voices
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    
    # Construct headers and endpoint
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY, 
        "Content-Type": "application/json", 
        "accept": "audio/mpeg"
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

    # Send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        print(e)
        return None  # Return None if an exception occurs

    # Handle response
    if response.status_code == 200:
        return response.content  # Handling response here if status is 200
    else:
        print(f"Failed to get audio: {response.status_code}, {response.text}")
        return None  # Optionally provide more detailed error info or handle other statuses
