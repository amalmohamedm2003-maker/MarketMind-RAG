import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "vectorstore/faiss_index/index.faiss"
META_PATH = "vectorstore/faiss_index/metadata.json"

class MarketingRetriever:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)
        with open(META_PATH) as f:
            self.metadata = json.load(f)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def retrieve(self, query, k=5):
        q_emb = self.model.encode([query], normalize_embeddings=True)
        D, I = self.index.search(np.array(q_emb), k)

        results = []
        for idx in I[0]:
            results.append(self.metadata[idx])

        return results
