from openai import OpenAI
client = OpenAI()
import json

data = "John Doe is a star developer. He is 30 years old and has a cat called Johnny"

data_prompt = f"""
Use the given text to extract the fields as a JSON object:

NAME
occupation
AGE
HAS_PET
IS_PLUMBER
PET_NAME

Use this unstructured data: {data}
"""

# Generating response back from gpt-3.5-turbo
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': data_prompt}]
)
print(openai_response.choices[0].message.content)
print(json.dumps(openai_response.choices[0].message.content))

# output:
# {
#   "NAME": "John Doe",
#   "occupation": "star developer",
#   "AGE": 30,
#   "HAS_PET": true,
#   "IS_PLUMBER": false,
#   "PET_NAME": "Johnny"
# }

