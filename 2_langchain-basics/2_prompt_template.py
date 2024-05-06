from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

client = ChatOpenAI()

# 1
query_prompt = PromptTemplate.from_template("What is your query: {query}")
query = query_prompt.format(query="Adam is 5 years older to Amy. How old is she? Amy's twin was born in 2000")
print(query)

res = client.invoke(query)
print("res", res.content)

# 2
client2 = ChatOpenAI(model="gpt-4")

prompt = PromptTemplate.from_template("Assume a {teacher} role. Explain to me about '{question}' in a simple three line summary")

question = prompt.format(teacher="science",question="3 body problem")

res = client2.invoke(question)

print(res)

