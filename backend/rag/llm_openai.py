from core.settings import OPENAI_API_KEY

class OpenAILLM:
    def __init__(self):
        self.enabled = bool(OPENAI_API_KEY)
        if self.enabled:
            from openai import OpenAI
            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, prompt: str) -> str:
        if not self.enabled:
            raise RuntimeError("OpenAI not configured")

        res = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
