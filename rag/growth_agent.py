from rag.retriever import MarketingRetriever
from rag.generator import generate_answer

class GrowthAgent:
    def __init__(self):
        self.retriever = MarketingRetriever()

    def analyze(self, question):
        docs = self.retriever.retrieve(question)

        context = "\n\n".join(
            [
                f"Source: {d['source']} | Channel: {d['channel']} | Metric: {d['metric']} | Text: {d['text']}"
                for d in docs
            ]
        )

        answer = generate_answer(context, question)

        return {
            "question": question,
            "insights": answer,
            "sources_used": len(docs)
        }
