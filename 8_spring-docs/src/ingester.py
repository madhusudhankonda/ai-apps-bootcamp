from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OllamaEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

CHROMA_DB = "./chroma_db"
MODEL = os.getenv("MODEL", "codellama")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
ollama_embeddings = OllamaEmbeddings(base_url=OLLAMA_BASE_URL, model=MODEL)

def get_all_chunks():
    loader = PyPDFDirectoryLoader("./data")
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap=10)
    chunks = splitter.split_documents(docs)
    print("Num of Chunks: ", len(chunks))
    return chunks

def vectorise_all():
    chunks = get_all_chunks()
    
    print("Storing all chunks")

    store = Chroma.from_documents(
        documents=chunks, 
        embedding=ollama_embeddings,
        persist_directory=CHROMA_DB)

    store.persist()
    print("All data vectorised in Chroma")

def get_store():
    store = Chroma(
        persist_directory=CHROMA_DB,
        embedding_function=ollama_embeddings)
    
    return store

def main():

    print("Using ", OLLAMA_BASE_URL)
    
    print('Vectorising ALL data')

    vectorise_all()

if __name__ == "__main__":
    main()

