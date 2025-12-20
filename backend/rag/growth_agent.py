from rag.retriever import MarketingRetriever
from rag.llm_router import LLMRouter
from rag.metrics import faithfulness

class GrowthAgent:
    def __init__(self):
        self.retriever = MarketingRetriever()
        self.llm = LLMRouter()

    def analyze(self, question: str):
        docs = self.retriever.retrieve(question)

        context = "\n".join(docs)
        prompt = f"""
You are a senior growth marketing expert.
Answer clearly and practically.

Context:
{context}

Question:
{question}
"""

        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "faithfulness": faithfulness(answer, context),
            "sources_used": len(docs)
        }
