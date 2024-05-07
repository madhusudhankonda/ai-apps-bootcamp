from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL_VERBOSE = os.getenv("MODEL_VERBOSE", False)
TEMPERATURE = os.getenv("TEMPERATURE", 0.7)

# , 'Code Llama 7B', 'Code Llama 13B', "Code Llama 34B", "Code Llama 70B"
model_choices = ('Llama 3', 'Llama 2', 'Mistral', 'Code Llama')

llm_llama3 = ChatOllama(
    model="llama3", 
    base_url=OLLAMA_BASE_URL, 
    verbose=MODEL_VERBOSE, 
    temperature=TEMPERATURE)
llm_llama2 = ChatOllama(
    model="llama2", 
    base_url=OLLAMA_BASE_URL, 
    verbose=MODEL_VERBOSE, 
    temperature=TEMPERATURE)
llm_mistral = ChatOllama(
    model="mistral", 
    base_url=OLLAMA_BASE_URL, 
    verbose=MODEL_VERBOSE, 
    temperature=TEMPERATURE)
llm_codellama = ChatOllama(
    model="codellama", 
    base_url=OLLAMA_BASE_URL, 
    verbose=MODEL_VERBOSE, 
    temperature=TEMPERATURE)


models = {
    'Llama 3': llm_llama3,
    'Llama 2': llm_llama2,
    'Mistral': llm_mistral,
    'Code Llama': llm_codellama
    }

# Choose the model
def get_model(model_name):
    model =  models.get(model_name, None)
    print("Chosen model: ", model)
    return model
