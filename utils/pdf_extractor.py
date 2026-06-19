import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path: str) -> dict:
    
    """
    Opens a PDF file and extracts text from each page.
    Returns a dict with page numbers as keys and text as values.
    """

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at path: {pdf_path}")

    doc = fitz.open(pdf_path)
    pages = {}

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        pages[page_num + 1] = text.strip()

    doc.close()
    return pages