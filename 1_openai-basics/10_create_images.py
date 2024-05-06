from openai import OpenAI
client = OpenAI()

res = client.images.generate(
  model="dall-e-3",
  prompt="Software Engineers having Fish and Chips at Devoxx Conference in London",
  n=1,
  size="1024x1024"
)

print(res)

