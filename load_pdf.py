import fitz  # PyMuPDF
import os

PDF_DIR = "finance_docs"

def load_pdfs():
    text = ""
    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            doc = fitz.open(os.path.join(PDF_DIR, file))
            # print(doc)
            print(f"Reading: {file}")
            for page in doc:
                # print(page)
                text += page.get_text()
    return text

data = load_pdfs()
# print(data)

# print("\nCharacters extracted:", len(data))
# print("\nSample text:\n")
# print(data[:1000])
