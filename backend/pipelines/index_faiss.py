import json
import faiss
import numpy as np
import os

CHUNKS_PATH = "data/processed/chunks.json"
EMBEDDINGS_PATH = "data/processed/embeddings.npy"
INDEX_PATH = "vectorstore/faiss_index"

os.makedirs(INDEX_PATH, exist_ok=True)

def build_index():
    with open(CHUNKS_PATH, "r") as f:
        chunks = json.load(f)

    embeddings = np.load(EMBEDDINGS_PATH)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    faiss.write_index(index, f"{INDEX_PATH}/index.faiss")

    with open(f"{INDEX_PATH}/metadata.json", "w") as f:
        json.dump(chunks, f, indent=2)

    print("✅ FAISS index built successfully")

if __name__ == "__main__":
    build_index()
