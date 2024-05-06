import openai
from openai import OpenAI

client = OpenAI()

file= open("./hello-devoxx.mp3", "rb")
transcription_file = audio = client.audio.transcriptions.create(
    model="whisper-1",
    file=file
)

print(transcription_file.text)