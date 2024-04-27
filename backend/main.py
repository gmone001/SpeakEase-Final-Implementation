# uvicorn main:app --reload
# uvicorn main:app
#source venv/bin/activate
from fastapi import FastAPI, File, UploadFile, HTTPException 
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware 
from decouple import config
import openai

# custom Function Imports from other files
from functions.openai_requests import convert_audio_to_text
from functions.openai_requests import get_chat_response
from functions.database import store_messages
from functions.database import reset_messages
from functions.text_to_speech import convert_text_to_speech

# Get .env Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

#initialize fastAPI
app = FastAPI()

# CORS origins for possible hosts, may have to change for IGOR
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

# CORS middleware to allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# reset conversation route 
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}

# get audio file from frontend and return audio response
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # # Get saved audio INITAL TEST to see if openAI and trnascribe works
    # audio_input = open("voice.mp3", "rb")

    #save file from frontend
    with open(file.filename,"wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # decode audio
    message_decoded = convert_audio_to_text(audio_input)

    #guard to ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="FAILED decoding audio")
    
    # receive chatgtp response
    chat_response = get_chat_response(message_decoded)

    print(chat_response)

    # Guard to ensure message decoded
    if not chat_response:
        return HTTPException(status_code=400, detail="FAILED to get chat response")
    
    # store messages in JSON file
    store_messages(message_decoded, chat_response)

    #convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)
    
    if not audio_output:
        return HTTPException(status_code=400, detail="FAILED to get 11 labs audio output")
    
    # create a generator to chunk of data
    def iterfile():
        # read audio output in chunks
        yield audio_output

    # return audio output as a streaming response
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
