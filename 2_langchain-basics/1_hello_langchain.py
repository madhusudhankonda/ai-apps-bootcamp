from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_core.messages import HumanMessage

q = "What is the element present in a banana?"

#1. Using OpenAI client
openai_client = OpenAI()

# Note that the openai client expects a string as the input
res = openai_client.invoke(q)

print(res)

#2. The ChatModel
chat_client = ChatOpenAI()

messages = [HumanMessage(content=q)]

res_msg = chat_client.invoke(messages)

# print(type(res_msg)) # prints: <class 'langchain_core.messages.ai.AIMessage'>
print(res_msg)

