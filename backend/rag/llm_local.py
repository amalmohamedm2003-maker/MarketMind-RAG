from transformers import pipeline
from loguru import logger

class LocalLLM:
    def __init__(self):
        logger.info("Loading local CPU LLM (flan-t5-base)")
        self.pipe = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            device=-1
        )

    def generate(self, prompt: str) -> str:
        out = self.pipe(prompt, max_length=256)
        return out[0]["generated_text"]
