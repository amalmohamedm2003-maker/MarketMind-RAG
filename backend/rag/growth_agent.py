from backend.rag.retriever import MarketingRetriever
from backend.rag.llm_router import LLMRouter
from backend.rag.prompts import BUSINESS_JSON_RAG_PROMPT
import json
import re

class GrowthAgent:
    def __init__(self):
        self.retriever = MarketingRetriever()
        self.llm = LLMRouter()

    def _safe_json_parse(self, text: str) -> dict:
        """
        Ensures frontend never crashes even if LLM returns extra text
        """
        try:
            match = re.search(r"\{.*\}", text, re.S)
            if match:
                return json.loads(match.group())
        except Exception:
            pass

        # fallback safe response
        return {
            "summary": "Unable to generate structured response with current model.",
            "key_insights": [],
            "recommendations": [],
            "metrics_impact": {},
            "confidence_level": "Low"
        }

    def analyze(self, question: str) -> dict:
        docs = self.retriever.retrieve(question, top_k=5)

        context = "\n".join(
            d if isinstance(d, str) else d.get("text", "")
            for d in docs
        )

        prompt = BUSINESS_JSON_RAG_PROMPT.format(
            context=context,
            question=question
        )

        raw_answer = self.llm.generate(prompt)
        structured = self._safe_json_parse(raw_answer)

        structured["sources_used"] = len(docs)
        return structured
