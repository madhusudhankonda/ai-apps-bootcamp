from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

template = """
    You are a helpful assistant. 
    Answer the following questions based on the
    history of the conversation provided as:

    history: {history}
    
    and the user's question as

    User's question: {question}
    """

prompt = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI()

chain = prompt | llm 

response = chain.invoke(
    {"history":"Flatwhite is made of flour mixed in olive oil", 
     "question":"How is Flatwhite made?"})

print(response)