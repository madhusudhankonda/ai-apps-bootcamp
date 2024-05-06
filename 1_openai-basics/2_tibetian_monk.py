import openai
from openai import OpenAI

# Use this format to explicitly mention the key 
# client = OpenAI(api_key="your-api-key")

# API Key is set as an environment variable 
client = OpenAI()


result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system", "content":"You are a Tibetan Monk - everything you answer is cryptic and short"},
        {"role":"user", "content":"What is life?"}
    ]
)
print(">>", result.choices[0].message.content)