from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(question: str, chunks: list) -> dict:
    context = ""
    sources = []

    for i, chunk in enumerate(chunks):
        context += f"\n[Source {i+1} - Page {chunk['page']}]:\n{chunk['text']}\n"
        sources.append(f"Page {chunk['page']}, Chunk {chunk['chunk_index']}")

    prompt = f"""You are a research assistant. Answer the question using ONLY the provided sources below.
If the answer is not found in the sources, say "This information is not available in the provided paper."
Always mention which source your answer comes from.

Sources:
{context}

Question: {question}

Answer:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": sources
    }