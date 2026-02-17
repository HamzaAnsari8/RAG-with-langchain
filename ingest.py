import os
from dotenv import load_dotenv

                            # UnstructuredFileLoader for scanned images pdf,messy,layout matters(table,forms, etc) and mixed documents
from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


load_dotenv()

PDF_DIR = "data"
VECTOR_DB_DIR = "vectordb"

#Loading  PDF
documents = []
for file in os.listdir(PDF_DIR):
    if file.lower().endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(PDF_DIR, file))
        documents.extend(loader.load())

print(f"Loaded {len(documents)} pages from PDFs")

#Text splitting
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

#Creating Embeddings 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Storing in vectorDB
Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=VECTOR_DB_DIR
)

print("✅ Data ingestion completed")
