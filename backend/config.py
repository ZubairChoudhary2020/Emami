import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CHROMA_PATH = os.getenv("CHROMA_PATH")
DOCS_PATH = os.getenv("DOCS_PATH")
print("GROQ KEY LOADED:", GROQ_API_KEY)