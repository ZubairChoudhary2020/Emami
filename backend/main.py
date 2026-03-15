import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from rag import ask_question
from ingest import ingest_documents

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Emami AI Knowledge Assistant</h1>
    <p>Service is running.</p>
    <a href="/docs">Open API Docs</a>
    """


@app.post("/ask")
def ask(q: Question):
    answer = ask_question(q.question)
    return {"answer": answer}


@app.post("/ingest")
def ingest():
    ingest_documents()
    return {"status": "Documents ingested successfully"}


@app.get("/health")
def health():
    return {"status": "healthy"}