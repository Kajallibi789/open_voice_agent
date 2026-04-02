from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.tts_service import text_to_speech

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Voice Agent Running"}

@app.get("/speak")
def speak(text: str):
    audio_file = text_to_speech(text)
    return FileResponse(audio_file, media_type="audio/wav")