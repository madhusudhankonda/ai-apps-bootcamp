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
from PIL import Image
from chroma_main import answer_with_retriever, answer_no_retriever

langchain.cache =  InMemoryCache()

load_dotenv()

CHROMA_DB = "./chroma_db"
MODEL = os.getenv("MODEL", "codellama")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
llm = ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL, temperature=0.0)
ollama_embeddings = OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model="codellama")

img = Image.open("./src/spring-bot.png")
size = (800, 200)
img = img.resize(size)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                    max-width: 800px; /* Adjust the maximum width as needed */
        padding: 0 20px; /* Add padding to the sides */
                }
        </style>
        """, unsafe_allow_html=True)
st.image(img,use_column_width=True)


col1,col2,col3,col4,col5,col6= st.columns(6)
with col1:
    option = st.selectbox(
        'Version',
        ('6.0', '5.3', '5.2'))

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is your query?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)    
    
    response = answer_no_retriever(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        # message_placeholder.markdown(response + "▌")
        message_placeholder.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
with col6:
    st.write("")
    st.button("clear history", type="primary")    
    if st.button:
        st.session_state.messages = []