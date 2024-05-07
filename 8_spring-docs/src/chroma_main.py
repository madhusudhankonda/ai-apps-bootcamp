import streamlit as st
import langchain
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough,RunnableLambda
from langchain_community.chat_models import ChatOllama
from langchain.cache import InMemoryCache
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
import os

langchain.cache =  InMemoryCache()

load_dotenv()

CHROMA_DB = "./chroma_db"
MODEL = os.getenv("MODEL", "codellama")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# OLLAMA_BASE_URL= "http://20.77.12.78:11434"

llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL)
ollama_embeddings = OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model=MODEL)

template = """
You are a Spring Framework Expert - an AI assistant for question-answering tasks. 

Use the following pieces of retrieved context to answer the question. 

If you don't know the answer, just say that you don't know. 

Make sure the answer is explained with examples. Mention the references/citations and the page numbers.

%CONTEXT%
{context}

%Question%
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)

def get_store():
    store = Chroma(
        persist_directory=CHROMA_DB,
        embedding_function=ollama_embeddings)

    return store

def answer_with_retriever(question):
    retriever = get_store().as_retriever(search_kwargs={"k":3})

    chain = (
        {"context":retriever, "question":RunnablePassthrough()}
        |prompt
        |llm
        |StrOutputParser()
    )
    try:
        results = chain.invoke(question)

        return results
    except:
        print("Exception")


def add_qa_context(question):
    search = get_store().similarity_search(question)
    
    context = "\n".join(s.page_content for s in search) 
    
    return context

def answer_no_retriever(question):
    print("Answering the question", question)
    print("Using model", MODEL)

    chain = (
    {"context":RunnableLambda(add_qa_context), "question":RunnablePassthrough()}
    |prompt
    |llm
    |StrOutputParser()
    )

    res = chain.invoke(question)
    # print("res",res)
    return res

