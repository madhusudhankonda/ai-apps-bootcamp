import ollama

response = ollama.chat(model='llama2', messages=[
  {
    "role": "user",
    "content": "What is Ollama?",
    "stream":False
  },
])
print(response["message"]["content"])