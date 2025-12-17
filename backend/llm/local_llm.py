from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from loguru import logger

class LocalLLM:
    def __init__(self):
        logger.info("Loading flan-t5-small (CPU)")
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=120,
                do_sample=False
            )

        text = self.tokenizer.decode(
            output[0],
            skip_special_tokens=True
        )

        logger.info(f"Local LLM output: {text}")
        return text
