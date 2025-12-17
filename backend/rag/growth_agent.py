from rag.generator import generate_answer
from rag.retriever import MarketingRetriever
from rag.metrics import faithfulness
from loguru import logger

class GrowthAgent:
    def __init__(self):
        self.retriever = MarketingRetriever()

    def analyze(self, question: str) -> dict:
        docs = self.retriever.retrieve(question)
        context = "\n".join(docs)

        answer = generate_answer(context, question)

        if not answer.strip():
            logger.warning("Using deterministic fallback answer")
            answer = (
                "CPA can be reduced by focusing on high-intent keywords, "
                "adding negative keywords, improving landing page relevance, "
                "and reallocating spend to high-performing campaigns."
            )

        score = faithfulness(answer, docs)

        return {
            "answer": answer,
            "faithfulness": round(score, 2),
            "sources_used": len(docs)
        }
