import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

index = faiss.read_index("vectorstore/faiss_index/index.faiss")

with open("vectorstore/faiss_index/metadata.json") as f:
    metadata = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "How can I reduce CPA in paid marketing?"
q_emb = model.encode([query], normalize_embeddings=True)

D, I = index.search(np.array(q_emb), k=3)

print("\nTop Results:\n")
for idx in I[0]:
    print(metadata[idx]["text"][:200], "\n---\n")
