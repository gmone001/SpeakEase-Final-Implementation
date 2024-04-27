import requests # import requests library to make HTTP requests
from decouple import config

ELEVEN_LABS_API_KEY = config('ELEVEN_LABS_API_KEY') #refreshed as of 26/4/24

# Eleven Labs - text to speech
def convert_text_to_speech(message):
    # define data body for request
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }
    
    # define voice from 11 labs api websites list of voices, 
    #looking for a voice that speaks spanish and english with a good accent
    #the one currently set is Argentina Women's voice
    voice_speakEase = "9oPKasc15pfAbMr7N6Gs" #take this from 11-labs voice library 
    
    # Construct headers and endpoint, from 11-labs api references
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY, 
        "Content-Type": "application/json", 
        "accept": "audio/mpeg"
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_speakEase}"

    # send request to 11-labs api
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        print(e)
        return None  # Return None if an exception occurs

    # handle response from 11-labs api and error handle
    if response.status_code == 200:
        return response.content  # Handling response here if status is 200
    else:
        print(f"Failed to get audio: {response.status_code}, {response.text}")
        return None  # Optionally provide more detailed error info or handle other statuses
