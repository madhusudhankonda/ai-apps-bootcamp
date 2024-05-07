import langchain
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.chat_models import ChatOllama

template = """
Question: {question}
"""
MODEL = "llama2"
OLLAMA_BASE_URL = "http://localhost:11434"


prompt = ChatPromptTemplate.from_template(template)

llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL)

chain = prompt | llm | StrOutputParser()

question = "What is bTC?"

res = chain.invoke(question)

print(res)
