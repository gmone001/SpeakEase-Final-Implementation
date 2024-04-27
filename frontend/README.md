#SpeakEase! Final Project - Graciella Monetti
  SpeakEase is a cutting-edge web application crafted to enhance language learning through interactive audio conversations. It enables users to engage in dialogues with a sophisticated chatbot, record their responses, play them back, and receive transcriptions powered by OpenAI's API. 
  Featuring a clean and intuitive interface built with React and TailwindCSS on the frontend, and a robust FastAPI with a Python backend, SpeakEase is specifically designed for language learners looking to practice and improve their speaking skills in a stress-free environment. Whether you're a beginner trying to overcome speaking anxiety or a seasoned learner aiming to refine your fluency, SpeakEase provides the tools necessary for effective language practice.
#Features!
  Audio Recording and Playback: Users can record their voice directly in the browser and play back their recordings.

  Audio Transcription: Leverages OpenAI's powerful API to convert speech to text in real time. Alongside 11-Labs API for realistic voice response.

  Dynamic Interaction: Utilizes React for responsive frontend interactions and TailwindCSS for modern, utility-first styling.

  Backend Services: FastAPI backend to handle audio data processing efficiently and securely.
#Technologies Used!
  Frontend: React.js, TypeScript, TailwindCSS

  Backend: FastAPI, Python

  APIs: OpenAI for speech-to-text services, FastAPI, ElevenLabsAPI.

  Other: .env for environment variable management, axios for HTTP requests.
#Getting Started!
  Prerequisites
  Node.js and npm
  Python 3.8+
  Pipenv or virtualenv for Python package management
#Clone the git Repository! 
  Depenencies!
    npm install
      virtualenv venv
      source venv/bin/activate
      pip install -r requirements.txt
      node
      npm -i -g yarn
      openai
      python decouple
      python multipart
      requests
      fastapi
      "uvicorn[standard]"
#start the FastAPI server!
  uvicorn main:app 
  uvicorn main:app --reload 
#Usage!
  Record: Use the record button in the UI to start and stop audio recordings.

  Playback: Play the recorded audio directly in the browser.

  Transcribe: Submit audio to the backend where it is processed and transcribed using OpenAI.
#Contact!
  Graciella Monetti 
  gmone001@gold.ac.uk




