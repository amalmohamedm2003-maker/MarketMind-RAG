"""
Simple faithfulness + relevance evaluation for RAG
"""

def faithfulness(answer: str, context_docs: list[str]) -> float:
    """
    Measures how much of the answer is grounded in retrieved context
    """
    hits = 0
    for doc in context_docs:
        if doc.lower()[:50] in answer.lower():
            hits += 1

    return round(hits / max(len(context_docs), 1), 2)


def relevance(answer: str, question: str) -> float:
    """
    Naive relevance check (keyword overlap)
    """
    q_words = set(question.lower().split())
    a_words = set(answer.lower().split())

    overlap = q_words.intersection(a_words)
    return round(len(overlap) / max(len(q_words), 1), 2)
