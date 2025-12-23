from sentence_transformers import SentenceTransformer
import numpy as np

def embed_chunks(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [c["text"] for c in chunks]

    embeddings = model.encode(
        texts,
        batch_size=16,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    return embeddings, chunks
