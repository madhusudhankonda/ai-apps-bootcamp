import openai
from openai import OpenAI

client = OpenAI()

audio = client.audio.speech.create(
    model="tts-1",
    input = "Hello, Devoxx! How is it going?",
    voice="fable",
    response_format="mp3"
)

print (audio.stream_to_file("hello-devoxx.mp3"))

