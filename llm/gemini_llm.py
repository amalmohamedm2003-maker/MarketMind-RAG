import google.generativeai as genai
import os
import time

class GeminiRouter:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)

        self.models = [
            "models/gemini-flash-lite-latest",
            "models/gemini-flash-latest"
        ]

        self._local_llm = None  # lazy load

    def _get_local_llm(self):
        if self._local_llm is None:
            print("⚠️ Loading local CPU LLM (first time only)...")
            from llm.local_llm import LocalLLM
            self._local_llm = LocalLLM()
        return self._local_llm

    def generate(self, prompt):
        for model_name in self.models:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.4,
                        "max_output_tokens": 600
                    }
                )
                return response.text
            except Exception as e:
                print(f"⚠️ Gemini failed on {model_name}: {str(e)[:120]}")
                time.sleep(2)

        # Fallback
        local_llm = self._get_local_llm()
        return local_llm.generate(prompt)
