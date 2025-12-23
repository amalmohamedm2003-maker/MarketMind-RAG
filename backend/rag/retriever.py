import os

CI_MODE = os.getenv("CI", "false") == "true"

import faiss
from sentence_transformers import SentenceTransformer
from backend.core.settings import FAISS_INDEX_PATH
from loguru import logger

class MarketingRetriever:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

        # ✅ NEW (CI-safe)
        if os.getenv("CI") == "true":
            self.index = None
            logger.warning("CI MODE – FAISS disabled")
            return

        if os.path.exists(FAISS_INDEX_PATH):
            self.index = faiss.read_index(FAISS_INDEX_PATH)
            logger.info("FAISS index loaded")
        else:
            self.index = None
            logger.warning("FAISS index missing – NO-INDEX MODE")

    def retrieve(self, query, top_k=5):
        if not self.index:
            return ["Mock document from CI"]

        vec = self.embedder.encode([query])
        _, idxs = self.index.search(vec, top_k)
        return [f"Doc {i}" for i in idxs[0]]
