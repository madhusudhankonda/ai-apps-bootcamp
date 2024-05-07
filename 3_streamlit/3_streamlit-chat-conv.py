import streamlit as st
from openai import OpenAI

st.title("Hello, Streamlit!")

client = OpenAI()

if prompt := st.chat_input():
    st.markdown("### Your Q:")
    st.write(">> ", prompt)

    result = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"You are an expert in BTC"},
            {"role":"user", "content":prompt}
        ]
    )
    st.markdown("### My A:")
    st.write(result.choices[0].message.content)