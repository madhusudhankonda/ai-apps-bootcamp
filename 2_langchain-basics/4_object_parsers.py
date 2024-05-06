from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import OpenAI

model = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.0)

# Define your desired data structure.
class Employee(BaseModel):
    salutation: str = Field(description="Mr if the Employee is Male or Mrs if Female")

# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=Employee)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
chain = prompt | model | parser

output = chain.invoke({"query": "John Smith"})

print(output)