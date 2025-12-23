from backend.pipelines.loaders.seo_loader import load_seo
from backend.pipelines.loaders.analytics_loader import load_analytics
from backend.pipelines.loaders.keywords_loader import load_keywords
from backend.pipelines.loaders.cases_loader import load_cases
from backend.pipelines.chunker import chunk_documents
from backend.pipelines.embedder import embed_chunks
from backend.pipelines.build_faiss import build_faiss

def run():
    documents = []
    documents += load_seo()
    documents += load_analytics()
    documents += load_keywords()
    documents += load_cases()

    if not documents:
        raise RuntimeError("❌ No documents loaded.")

    chunks = chunk_documents(documents)
    embeddings, metadata = embed_chunks(chunks)
    build_faiss(embeddings, metadata)

    print("✅ MarketMind ingestion completed")

if __name__ == "__main__":
    run()
