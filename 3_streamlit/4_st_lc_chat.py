import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

st.title("Hello, Streamlit!")

if prompt := st.chat_input():
    st.markdown("### Your Q:")
    st.write(">> ", prompt)

    res = llm.invoke(prompt)

    st.markdown("### My A:")
    st.write(res)