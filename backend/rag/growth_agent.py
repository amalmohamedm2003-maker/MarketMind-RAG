from rag.retriever import MarketingRetriever
from rag.llm_router import LLMRouter
from rag.prompts import BUSINESS_RAG_PROMPT

class GrowthAgent:
    def __init__(self):
        self.retriever = MarketingRetriever()
        self.llm = LLMRouter()

    def analyze(self, question: str):
        docs = self.retriever.retrieve(question, top_k=5)

        if not docs:
            return {
                "answer": "Insufficient data to provide a confident recommendation.",
                "faithfulness": 0,
                "sources_used": 0,
            }

        context = "\n".join(f"- {d}" for d in docs)

        prompt = BUSINESS_RAG_PROMPT.format(
            context=context,
            question=question
        )

        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "faithfulness": 1,
            "sources_used": len(docs),
        }
