from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from utils.pdf_extractor import extract_text_from_pdf
from utils.chunker import chunk_text
from utils.embedder import embed_chunks, embed_query
from utils.vector_store import build_index, search_index
from utils.qa_engine import generate_answer

app = FastAPI(title="Research Shastra AI", version="1.0")

UPLOAD_DIR = "uploaded_papers"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Research Shastra AI is running"}


@app.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    """
    Accepts a PDF file.
    Extracts text, chunks it, embeds chunks, builds FAISS index.
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    pages = extract_text_from_pdf(file_path)
    chunks = chunk_text(pages)
    embeddings, chunks = embed_chunks(chunks)
    build_index(embeddings, chunks)

    return {
        "message": "Paper indexed successfully",
        "filename": file.filename,
        "total_pages": len(pages),
        "total_chunks": len(chunks)
    }


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Accepts a question.
    Retrieves relevant chunks, generates cited answer.
    """
    query_embedding = embed_query(request.question)
    relevant_chunks = search_index(query_embedding)
    result = generate_answer(request.question, relevant_chunks)

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }