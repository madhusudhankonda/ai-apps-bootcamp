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
    st.write("Your q")
    st.write(question)

    res = get_response(question)

    st.markdown(res.content)
