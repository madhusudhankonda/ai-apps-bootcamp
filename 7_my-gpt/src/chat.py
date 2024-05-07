from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough,RunnableLambda
from langchain.schema.output_parser import StrOutputParser

from models import get_model

template = """
You are an AI assistant for question-answering tasks. 

Answer the questions based Make sure the answer is explained in about 400 words. 

Mention the references/citations and the page numbers.

%Question%
{question}

Answer:
"""

coding_template = """
You are a coding AI assistant for question-answering tasks on coding. 

Make sure you provide all answers with example code. 

%Question%
{question}

Answer:
"""

qna_prompt = ChatPromptTemplate.from_template(template)
coding_prompt = ChatPromptTemplate.from_template(coding_template)

def generate_response(prompt_input, model_name):
    llm = get_model(model_name)
    
    if model_name == "Code Llama":
        prompt = coding_prompt
        print(prompt)
    else:
        prompt = qna_prompt

    chain = (prompt | llm | StrOutputParser())
    
    res = chain.invoke({"question":prompt_input})

    return res
