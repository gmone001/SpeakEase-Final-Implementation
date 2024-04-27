import openai
from decouple import config

# Import custom functions
from functions.database import get_recent_messages

# Retrieve environment variables
openai.organization = config('OPEN_AI_ORG')
openai.api_key = config('OPEN_AI_KEY')


# Convert audio to text using OpenAI Whisper
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript['text']
        return message_text
    except Exception as e:
        print(e)
        return None
   
# OpenAI Chat - Chat GPT
# Get response to our message
def get_chat_response(message_input):
    # Decode audio file, decoded to text, provide latest message
    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(e)
        return
