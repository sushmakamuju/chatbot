from dotenv import load_dotenv
import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Load embeddings (already used during indexing)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS index
vectorstore = FAISS.load_local(
    "finance_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Initialize Groq LLM (API key from .env)
llm = ChatGroq(
    model=os.getenv("MODEL_ID"),
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

print("💰 Finance RAG Chatbot ready. Type 'exit' to quit.\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    # Retrieve relevant chunks
    docs = vectorstore.similarity_search(query, k=4)

    # Build context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Prompt LLM with retrieved context
    prompt = f"""
You are a finance assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    print("\nBot:", response.content, "\n")
