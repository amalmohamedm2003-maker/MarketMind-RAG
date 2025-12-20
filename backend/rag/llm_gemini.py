from core.settings import GEMINI_API_KEY

class GeminiLLM:
    def __init__(self):
        self.enabled = bool(GEMINI_API_KEY)
        if self.enabled:
            import google.generativeai as genai
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate(self, prompt: str) -> str:
        if not self.enabled:
            raise RuntimeError("Gemini not configured")

        res = self.model.generate_content(prompt)
        return res.text
