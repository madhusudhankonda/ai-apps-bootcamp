import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

st.title("My Own Chatbot - with LangChain")

llm = ChatOpenAI()

def get_response(prompt):
    messages = [
        SystemMessage(content="You are Uncle Bob"),
        HumanMessage(content=prompt)
    ]
    reply = llm.invoke(messages)

    return reply

if question := st.chat_input():
    st.chat_message("user").write(question)

    res = get_response(question)

    st.chat_message("assistant").write(res.content)
