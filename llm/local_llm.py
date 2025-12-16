from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class LocalLLM:
    def __init__(self):
        model_name = "google/flan-t5-small"

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            force_download=True
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name,
            force_download=True
        )

    def generate(self, prompt, max_tokens=256):
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens
        )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )
