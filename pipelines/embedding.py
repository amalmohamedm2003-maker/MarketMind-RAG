import json
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

CHUNKS_PATH = "data/processed/chunks.json"
EMBEDDINGS_PATH = "data/processed/embeddings.npy"

def generate_embeddings():
    with open(CHUNKS_PATH, "r") as f:
        chunks = json.load(f)

    texts = [c["text"] for c in chunks]

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(
        texts,
        batch_size=16,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    np.save(EMBEDDINGS_PATH, embeddings)
    print("✅ Embeddings generated successfully")

if __name__ == "__main__":
    generate_embeddings()
