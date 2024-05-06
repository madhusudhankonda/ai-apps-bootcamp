from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser,CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate

#1. String Parser

client = ChatOpenAI()
# str_parser = StrOutputParser()

# prompt = ChatPromptTemplate.from_template("Give me a recipe for {recipe}")

# chain = prompt | client | str_parser

# res = chain.invoke({"recipe":"Dosa"})

# print(res)

############---------------------------###########

# 2. CSV Parser

csv_parser = CommaSeparatedListOutputParser()

format_instructions = csv_parser.get_format_instructions()

prompt = PromptTemplate(
    template="Latest trends in {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": format_instructions},
)

model = ChatOpenAI(temperature=0)

chain = prompt | model | csv_parser

latest_trends = chain.invoke({"topic":"AI"})

print(latest_trends)