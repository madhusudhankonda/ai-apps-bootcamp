# Module 2: Introduction to Langchain 

In this module, we will look at what is Langchain and how it can be leveraged to develop and deploy AI powered software applications. 

As expected, we need two pre-requisites to be performed before we start on this lab:

- The setup file (`setup.sh`) is executed so the `.venv` gets provisioned. As part of the script, the requirements file will also be executed so the required modules gets added to the project

- The OpenAPI Key environment variable is set and you export the API Key (`OPENAI_API_KEY`) as an environment variable.

``` 
export OPENAI_API_KEY=<your-key>
```

> The `requirements.txt` file consists of two modules `langchain` and `langchain-openai` that would be downloaded as part of the setup

Once the environment is ready, let's start the Hello World program!

## Hello World

As a first application, we will simply ask the OpenAI LLM a question. If all goes well, we will receive an answer.

> Langchain has two flavours of LLMs - the LLM with a class defined as `OpenAI` (duh!) and chat based LLM called `ChatOpenAI`. The LLM objects take in String and respond with a String. The ChatModels take in a list of messages and outputs a message.


Let's create a simple Hello World python program to ask a question to OpenAI's LLM. We use a `gpt-4` model in this example.

Let's import the required library first and create a client:

```
from openai import OpenAI

client = OpenAI()
```

We will now invoke a completions endpoint to invoke the model. The `openapi` SDK provides a convenient way of invoking the RESTFul endpoint `client.chat.completions.create(...)`. The create method will take a few parameters such as model and the model messages.

The following code snippet shows the chat completion code in action:

```
result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system", "content":"You are an expert in Cryptocurrencies, especially Bitcoin"},
        {"role":"user", "content":"Explain, what is BTC in three lines"}
    ]
)
```
The `model` attribute is where you'd provide which model you want to invoke - `gpt-4` or `gpt-3.5-turbo`, for example. 

The `messages` attribute expects an array of json objects that define the `system`, `assistant` and `user` roles and respective instructions.

The complete code is available at ![]() but here's it is for completeness:

```
from openai import OpenAI

# Use this format to explicitly mention the key 
# client = OpenAI(api_key="your-api-key")

# API Key is set as an environment variable 
client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system", "content":"You are an expert in Cryptocurrencies, especially Bitcoin"},
        {"role":"user", "content":"Explain what is BTC in three lines"}
    ]
)
print(">>", result.choices[0].message.content)
```

Executing the `python 1_hello_world.py` should output the LLM's response to our question "Explain what is BTC in three lines".

## Giving a Personality to your LLM


