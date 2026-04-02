import subprocess
import uuid
import os

PIPER_PATH = "piper.exe"
MODEL_PATH = "models/en_US-lessac-medium.onnx"

def text_to_speech(text: str) -> str:
    output_file = f"audio_{uuid.uuid4().hex}.wav"

    command = [
        PIPER_PATH,
        "--model", MODEL_PATH,
        "--output_file", output_file
    ]

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    process.communicate(input=text)

    return output_file