import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

st.title("My Own Chatbot - with LangChain")

llm = ChatOpenAI()

if "messages" not in st.session_state.keys():
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
# else:
#     print("Exception..")

for result in st.session_state.messages:
    st.chat_message(result["role"]).write(result["content"])

def get_response(prompt):
    messages = [
        SystemMessage(content="You are a helpful assistant"),
        HumanMessage(content=prompt)
    ]

    return llm.invoke(messages)

# Overriding chat prompts
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)
    
    response = get_response(prompt)

    result = response.content

    # Capture ASSISTANT's Answers
    st.session_state.messages.append({"role": "assistant", "content": result})

    st.chat_message("assistant").write(result)

