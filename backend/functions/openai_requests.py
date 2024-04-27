import openai
from decouple import config 

# import custom functions from other files
from functions.database import get_recent_messages

#get environment variables from .env file
openai.organization = config('OPEN_AI_ORG')
openai.api_key = config('OPEN_AI_KEY')


# converting audio to text using OpenAI Whisper
def convert_audio_to_text(audio_file):
    try:
        #transcribe audio file from openai whisper api references
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript['text']
        return message_text
    except Exception as e:
        print(e)
        return None
   
# OpenAI Chata - Chat GPT
#get response to our message from our chatbot 
def get_chat_response(message_input):
    #decode audio file, decoded to text, provide latest message
    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print(messages)

    try:
        #get response from openai chat completion api 3.5 is the cheapest model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=messages
        )
        #from chatopenai api refeerences, get the first choice and the message content
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(e)
        return
