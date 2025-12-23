def test_retriever_runs_without_index():
    """
    CI-safe test:
    - Does NOT assume FAISS index exists
    - Verifies retriever fails gracefully
    """

    from backend.rag.retriever import MarketingRetriever

    retriever = MarketingRetriever()

    # Should not crash even if FAISS index is missing
    docs = retriever.retrieve("test query")

    assert isinstance(docs, list)
