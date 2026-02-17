from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

VECTOR_DB_DIR = "vectordb"

# calling embeddings model 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# loading vector DB
vectorstore = Chroma(
    persist_directory=VECTOR_DB_DIR,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0.3
)

#prompt
prompt = ChatPromptTemplate.from_template(
    """Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""
)

parser = StrOutputParser()

#RAG operation
def rag(question: str):
    print("🔍 Retrieving relevant chunks...")
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    chain = prompt | llm | parser

    print("🤖 Generating answer...")
    return chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

# query
if __name__ == "__main__":
    query = "Summarize the key points from both documents"
    answer = rag(query)

    print("\n🧠 ANSWER:\n")
    print(answer)

