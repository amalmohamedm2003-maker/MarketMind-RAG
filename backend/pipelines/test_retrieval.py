import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

def test_retriever_runs():
    from backend.rag.retriever import MarketingRetriever
    r = MarketingRetriever()
    docs = r.retrieve("test")
    assert isinstance(docs, list)


with open("vectorstore/faiss_index/metadata.json") as f:
    metadata = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "How can I reduce CPA in paid marketing?"
q_emb = model.encode([query], normalize_embeddings=True)

D, I = index.search(np.array(q_emb), k=3)

print("\nTop Results:\n")
for idx in I[0]:
    print(metadata[idx]["text"][:200], "\n---\n")
