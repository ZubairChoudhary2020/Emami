content = """import os
import shutil
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import CHROMA_PATH, DOCS_PATH

def ingest_documents():
    documents = []
    for f in os.listdir(DOCS_PATH):
        path = os.path.join(DOCS_PATH, f)
        if f.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
        elif f.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
            documents.extend(loader.load())
    if not documents:
        print("No documents found.")
        return
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH, ignore_errors=True)
    Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=CHROMA_PATH)
    print("Documents ingested successfully!")

if __name__ == "__main__":
    ingest_documents()
"""

with open("ingest.py", "w", encoding="utf-8") as f:
    f.write(content)

print("ingest.py written successfully!")
