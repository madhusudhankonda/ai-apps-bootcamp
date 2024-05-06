from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

client = ChatOpenAI()

prompt = ChatPromptTemplate.from_template("Give me a recipe for {recipe} as a summary in a bullet list format")

chain = prompt|client

res = chain.invoke({"recipe":"Mince Pie"})

print(res)