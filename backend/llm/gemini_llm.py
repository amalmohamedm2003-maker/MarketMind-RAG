from loguru import logger
import os

class GeminiRouter:
    def __init__(self):
        self.gemini_enabled = bool(os.getenv("GOOGLE_API_KEY"))

    def generate(self, prompt: str) -> str | None:
        # 1️⃣ Try Gemini
        if self.gemini_enabled:
            try:
                from llm.gemini_remote import GeminiRemote
                logger.info("Trying Gemini API")
                return GeminiRemote().generate(prompt)
            except Exception as e:
                logger.warning(f"Gemini failed: {e}")

        # 2️⃣ Try local LLM
        try:
            from llm.local_llm import LocalLLM
            logger.info("Trying local LLM")
            return LocalLLM().generate(prompt)
        except Exception as e:
            logger.error(f"Local LLM failed: {e}")

        # 3️⃣ Hard fallback
        logger.error("All LLMs failed")
        return None
