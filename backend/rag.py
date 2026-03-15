from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config import CHROMA_PATH, GROQ_API_KEY


def ask_question(question: str):

    try:

        # Load embedding model
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Connect to Chroma vector database
        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embeddings
        )

        # Retrieve relevant documents
        docs = db.similarity_search(question, k=3)

        # Combine document text
        context = "\n".join([doc.page_content for doc in docs])

        # Prompt template
        template = """
You are a helpful assistant answering questions from company policy documents.

Use ONLY the context provided below to answer.

Context:
{context}

Question:
{question}

Answer:
"""

        prompt = PromptTemplate.from_template(template)

        final_prompt = prompt.format(
            context=context,
            question=question
        )

        # Initialize Groq LLM
        llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
        )

        # Generate response
        response = llm.invoke(final_prompt)

        return response.content

    except Exception as e:
        print("ERROR OCCURRED:", str(e))
        return str(e)