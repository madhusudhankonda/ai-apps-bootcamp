import streamlit as st
import os

from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_history_aware_retriever,create_retrieval_chain

from langchain.chains.combine_documents import create_stuff_documents_chain

from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Website Chat",layout="centered")
st.title("Website Chat")

MODEL = os.getenv("MODEL", "llama2")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL)
ollama_embeddings = OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model=MODEL)

def get_vectorstore(url):
    loader = WebBaseLoader(url)
    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    chunks = text_splitter.split_documents(documents=document)

    vector_store = Chroma.from_documents(chunks, ollama_embeddings)
    return vector_store

def get_retriever_chain(vector_store):
    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","{input}"),
        ("user","Consider the full conversation to generate a search query to fetch the relevant results")
    ])

    chain = create_history_aware_retriever(llm, retriever, prompt=prompt)
    
    return chain

def get_conversational_rag_chain(retriever_chain): 
    
    prompt = ChatPromptTemplate.from_messages([
      ("system", "Answer the user's questions based on the below context:\n\n{context}"),
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
    ])
    
    stuff_documents_chain = create_stuff_documents_chain(llm,prompt)
    
    return create_retrieval_chain(retriever_chain, stuff_documents_chain)

def get_response(user_query):
    retriever_chain = get_retriever_chain(st.session_state.vector_store)
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    
    response = conversation_rag_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_query
    })
    
    return response['answer']


url = st.text_input("URL")
if url is None or url == "":
    st.info("Please enter a website URL in the sidebar")
else:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="I am an AI Assistant, How can I help you!")
        ]

    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore(url)    

    user_query = st.chat_input("What is your query?")

    if user_query is not None:
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        if isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)