# # app/main.py

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "RAG API Running"}

# app/main.py

from fastapi import FastAPI, UploadFile
import shutil

from app.extractor import extract_text
from app.chunker import chunk_text
from app.embeddings import create_embedding
from app.vector_store import (
    store_embeddings,
    search
)
from app.rag import ask_llm

app = FastAPI()


# Home Route
@app.get("/")
def home():

    return {
        "message": "RAG Chatbot Running"
    }


# Upload Route
@app.post("/upload")
async def upload(file: UploadFile):

    # Save uploaded file
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text(file_path)

    # Chunk text
    chunks = chunk_text(text)

    # Generate embeddings
    embeddings = []

    for chunk in chunks:

        emb = create_embedding(chunk)

        embeddings.append(emb)

    # Store in FAISS
    store_embeddings(chunks, embeddings, file.filename)

    return {
        "message": "Document uploaded successfully",
        "chunks": len(chunks)
    }


# Chat Route 
@app.post("/chat")
async def chat(query: str):

    # Create query embedding
    query_embedding = create_embedding(query)

    # Search relevant chunks
    results = search(query_embedding)

    chunks = results["documents"][0]

    metadata = results["metadatas"][0]

    print("Retrieved Chunks:", chunks)

    # Build context
    context = "\n".join(chunks)

    # Generate answer
    answer = ask_llm(context, query)

    return {
        "answer": answer,
        "sources": metadata
    }

