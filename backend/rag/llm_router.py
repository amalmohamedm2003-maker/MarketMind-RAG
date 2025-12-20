from loguru import logger
from core.settings import LLM_PROVIDER
from rag.llm_local import LocalLLM
from rag.llm_gemini import GeminiLLM
from rag.llm_openai import OpenAILLM

class LLMRouter:
    def __init__(self):
        self.local = LocalLLM()
        self.gemini = GeminiLLM()
        self.openai = OpenAILLM()

    def generate(self, prompt: str) -> str:
        if LLM_PROVIDER in ("auto", "gemini"):
            try:
                return self.gemini.generate(prompt)
            except Exception as e:
                logger.warning(f"Gemini failed: {e}")

        if LLM_PROVIDER in ("auto", "openai"):
            try:
                return self.openai.generate(prompt)
            except Exception as e:
                logger.warning(f"OpenAI failed: {e}")

        logger.warning("Falling back to local CPU LLM")
        return self.local.generate(prompt)
