import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag import ask_question
from ingest import ingest_documents

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Emami AI Assistant is running"}

@app.post("/ask")
def ask(q: Question):
    result = ask_question(q.question)
    return result

@app.post("/ingest")
def ingest():
    ingest_documents()
    return {"status": "Documents ingested successfully"}

@app.get("/health")
def health():
    return {"status": "healthy"}