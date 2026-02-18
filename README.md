# 📚 RAG with LangChain and Gemini API

This project implements a Retrieval-Augmented Generation (RAG) system using LangChain and Google Gemini API. It allows users to query their own documents by retrieving relevant context from a vector database and generating accurate answers using Gemini. The project is intentionally simple and focuses on two core scripts: ingest.py and retr_and_gen.py.

## 🚀 Features
- Document ingestion and preprocessing  
- Text chunking and embedding using Gemini  
- Vector database storage  
- Semantic search and retrieval  
- Context-aware response generation  
- Modular and easy-to-extend design  

## 🧠 Project Structure
RAG-with-LangChain-Gemini/  
├── data/                  # Input documents (PDF / TXT / DOCX)  
├── vectordb/              # Stored vector embeddings  
├── ingest.py              # Document ingestion & embedding  
├── retr_and_gen.py        # Retrieval and answer generation  
├── requirements.txt       # Python dependencies  
├── .env                   # Environment variables  
└── README.md              # Project documentation  

## 🛠️ Tech Stack
- Python 3.9+  
- LangChain  
- Google Gemini API  
- Vector Store (Chroma / FAISS)  
- python-dotenv  

## 🔐 Environment Setup
Create a `.env` file in the project root directory and add your Gemini API key:

GOOGLE_API_KEY="your_gemini_api_key_here"  

## 📦 Installation
1. Clone the repository  
git clone https://github.com/HamzaAnsari8/rag-langchain-gemini.git  
cd rag-langchain-gemini  

2. Create and activate a virtual environment  
python -m venv venv  
source venv/bin/activate      # Linux / macOS  
venv\Scripts\activate         # Windows  

3. Install dependencies  
pip install -r requirements.txt  

## 📥 Document Ingestion (ingest.py)
This script loads documents from the data folder, splits them into chunks, generates embeddings using Gemini, and stores them in a vector database. Run this script whenever documents are added or updated.

python ingest.py  

## 🔍 Retrieval and Generation (retr_and_gen.py)
This script takes a user query, retrieves relevant document chunks from the vector database, and generates a final response using Gemini.

python retr_and_gen.py  

Example:  
Enter your query: What is Retrieval Augmented Generation?  
Answer: Retrieval Augmented Generation (RAG) is a technique that combines information retrieval with large language models to produce accurate, context-aware responses.

## 🔁 RAG Workflow
1. Documents are ingested and converted into embeddings  
2. User submits a query  
3. Relevant document chunks are retrieved  
4. Gemini generates an answer using the retrieved context  

## 📌 Use Cases
- Chat with PDFs and text documents  
- Internal knowledge base assistant  
- Research and academic support  
- Enterprise document search  
- AI-powered FAQ systems  

## ⚠️ Notes
- Place documents inside the data directory before running ingestion  
- Re-run ingest.py whenever documents change  
- Gemini API usage may incur costs  

## 🔮 Future Enhancements
- Web UI using Streamlit or FastAPI  
- Conversational memory support  
- Streaming responses  
- Metadata-based filtering  
- Cloud-hosted vector databases  


## 👨‍💻 Author
Hamza Ansari
GitHub: https://github.com/HamzaAnsai8 
