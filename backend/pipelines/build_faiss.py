import faiss
import json
import numpy as np
from pathlib import Path

VECTOR_DIR = Path("backend/data/vectorstore")
VECTOR_DIR.mkdir(parents=True, exist_ok=True)


def build_faiss(embeddings: np.ndarray, metadata: list):
    if embeddings.ndim != 2 or embeddings.shape[0] == 0:
        raise RuntimeError(
            f"❌ Invalid embeddings shape: {embeddings.shape}"
        )

    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    faiss.write_index(index, str(VECTOR_DIR / "index.faiss"))

    with open(VECTOR_DIR / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"✅ FAISS index built with {embeddings.shape[0]} vectors")
