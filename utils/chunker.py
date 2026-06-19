def chunk_text(pages: dict, chunk_size: int = 512, overlap: int = 50) -> list:
    """
    Takes pages dict from pdf_extractor.
    Returns list of chunks with text, page number, and index.
    """
    chunks = []
    chunk_index = 0

    for page_num, text in pages.items():
        words = text.split()
        
        start = 0
        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)
            
            if chunk_text.strip():
                chunks.append({
                    "text": chunk_text,
                    "page": page_num,
                    "chunk_index": chunk_index
                })
                chunk_index += 1
            
            start = end - overlap

    return chunks