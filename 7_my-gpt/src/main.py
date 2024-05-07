import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os
from dotenv import load_dotenv

from models import get_model, model_choices
from chat import generate_response
load_dotenv()

st.set_page_config(page_title="MyGPT")
st.write("# MyGPT - a Single Chat App with Multiple Models")
st.markdown("""#### Chat Application with Multiple LLMs. 
- Choose a LLM of your choice from the dropdown in the left side menu bar. 
- Ask me any question. I will answer you using your model of choice. 
- For coding questions, choose Code Llama. I will assist you writing code too! """)
            

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "What do you want to ask me?"}]

if "selected_model_instance" not in st.session_state:
    st.session_state.selected_model_instance = None

# Functions
def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})

def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Sidebar for model selection
with st.sidebar:
    st.title('Settings')
    selected_model = st.selectbox("Choose your model", model_choices)
    st.session_state.selected_model_name = selected_model

# Main chat interface
display_messages()

if prompt := st.chat_input():
    add_message("user", prompt)
    with st.spinner(f"Getting the answer ..."):
        response = generate_response(prompt, st.session_state.selected_model_name)
        add_message("assistant", response)
    display_messages()
