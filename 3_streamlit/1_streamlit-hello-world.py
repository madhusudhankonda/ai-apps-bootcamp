import streamlit as st

st.title("Hello, Streamlit!")

if prompt := st.chat_input():
    st.markdown("### Your Q:")
    st.write(">> ", prompt)
    st.markdown("### My A:")
    st.write(">> ", "That's cool... so here's what I can tell you..")