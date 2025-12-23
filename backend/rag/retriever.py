import os
import faiss
from sentence_transformers import SentenceTransformer
from backend.core.settings import FAISS_INDEX_PATH
from loguru import logger

class MarketingRetriever:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

        if os.path.exists(FAISS_INDEX_PATH):
            self.index = faiss.read_index(FAISS_INDEX_PATH)
            logger.info("FAISS index loaded")
        else:
            self.index = None
            logger.warning("FAISS index missing – NO-INDEX MODE")

    def retrieve(self, query, top_k=5):
        if not self.index:
            return []

        vec = self.embedder.encode([query])
        _, idxs = self.index.search(vec, top_k)
        return [f"Doc {i}" for i in idxs[0]]

    def add_documents(self, texts, embeddings):
        self.index.add(embeddings)
        self.texts.extend(texts)
