from loguru import logger
from backend.core.settings import LLM_PROVIDER
from backend.rag.llm_local import LocalLLM
from backend.rag.llm_gemini import GeminiLLM
from backend.rag.llm_openai import OpenAILLM
from backend.rag.llm_ollama import OllamaLLM

class LLMRouter:
    def __init__(self):
        self.local = LocalLLM()
        self.gemini = GeminiLLM()
        self.openai = OpenAILLM()
        self.ollama = OllamaLLM()

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
        if LLM_PROVIDER in ("auto", "ollama"):
            try:
                return self.ollama.generate(prompt)
            except Exception as e:
                logger.warning(f"Ollama failed: {e}")

        logger.warning("Falling back to local CPU LLM")
        return self.local.generate(prompt)

