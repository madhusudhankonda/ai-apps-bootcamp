from openai import OpenAI

# Use this format to explicitly mention the key 
# client = OpenAI(api_key="your-api-key")

# API Key is set as an environment variable 
client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system", "content":"You are an expert in Cryptocurrencies, especially Bitcoin"},
        {"role":"user", "content":"Explain, what is BTC in three lines"}
    ]
)
print(">>", result.choices[0].message.content)