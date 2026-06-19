import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "faiss_index.bin"
CHUNKS_PATH = "chunks.pkl"

def build_index(embeddings: np.ndarray, chunks: list):
    """
    Builds FAISS index from embeddings.
    Saves index and chunks to disk.
    """
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)


def search_index(query_embedding: np.ndarray, top_k: int = 5) -> list:
    """
    Loads FAISS index, searches for top_k similar chunks.
    Returns list of matching chunk dicts.
    """
    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    distances, indices = index.search(query_embedding, top_k)

    results = []
    for i in indices[0]:
        if i != -1:
            results.append(chunks[i])

    return results