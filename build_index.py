import fitz
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PDF_DIR = "finance_docs"

def load_pdfs():
    text = ""
    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            doc = fitz.open(os.path.join(PDF_DIR, file))
            for page in doc:
                text += page.get_text()
    return text

print("Loading PDF...")
raw_text = load_pdfs()

print("Splitting text...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200
)
chunks = splitter.split_text(raw_text)
print(f"Total chunks: {len(chunks)}")

print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_texts(chunks, embeddings)
vectorstore.save_local("finance_index")

print("✅ Vector index created and saved")
