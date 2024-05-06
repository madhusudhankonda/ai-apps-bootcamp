from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

client = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a hopeless chef. You provide all rubbish recipes to your clients but sound very authentic"),
    ("human", "{question}")
    ]
)

p = prompt.format_messages(question="Give me a recipe for Banana Dosa")

print(p)

res = client.invoke(p)

print(res.content)

#2. Currency conversion

currency_template = ChatPromptTemplate.from_messages([
    ("system","You are a currency converter"),
    ("human", "Convert {unit} from {currency1} into {currency2}")
])

result = client.invoke(currency_template.format_messages(unit=5, currency1="GBP", currency2="USD"))

print(result.content)