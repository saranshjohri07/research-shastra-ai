# Research Shastra AI — Agentic AI Research Copilot

An agentic AI research copilot that enables citation-grounded Q&A on research papers using RAG, embeddings, vector search, and LLM reasoning.

---

## What it does

- Upload any research paper PDF
- Ask questions about the paper in natural language
- Get cited answers grounded in the paper — no hallucination
- Sources returned with every answer showing exact page and chunk references

---

## Architecture

```
PDF Upload → Text Extraction → Chunking → Embeddings → FAISS Index
Question → Embed Query → FAISS Search → Top-5 Chunks → LLM → Cited Answer
```

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| PDF Extraction | PyMuPDF (fitz) |
| Chunking | Custom fixed-size with overlap |
| Embeddings | SentenceTransformers (all-MiniLM-L6-v2) |
| Vector Store | FAISS (IndexFlatL2) |
| LLM | Groq (llama-3.3-70b-versatile) |
| Server | Uvicorn |

---

## Project Structure

```
research-shastra-backend/
├── main.py                  # FastAPI app, routes
├── utils/
│   ├── pdf_extractor.py     # PyMuPDF text extraction
│   ├── chunker.py           # Fixed-size chunking with overlap
│   ├── embedder.py          # SentenceTransformers embeddings
│   ├── vector_store.py      # FAISS index build and search
│   └── qa_engine.py         # LLM prompt and answer generation
├── .env                     # API keys (not committed)
├── .gitignore
└── requirements.txt
```

## Versions

| Version | Status | Description |
|---|---|---|
| V1 | ✅ Complete | Naive RAG — PDF upload, chunking, embeddings, FAISS, cited Q&A |
| V2 | 🔄 In Progress | Multi-agent system with LangGraph — Planner, Retriever, Reasoner, Citation, Explainer agents |
| V3 | 📅 Planned | Production engineering — PostgreSQL, Redis, Docker, auth, streaming |
| V4 | 📅 Planned | Advanced features — cross-paper comparison, research gap detection, equation explainer |

---
