from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks: list) -> tuple:
    """
    Takes list of chunk dicts from chunker.
    Returns embeddings as numpy array and original chunks list.
    """
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")
    
    return embeddings, chunks


def embed_query(query: str) -> np.ndarray:
    """
    Embeds a single query string.
    Used at retrieval time when user asks a question.
    """
    embedding = model.encode([query])
    return np.array(embedding).astype("float32")