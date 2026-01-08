import requests
from loguru import logger

class OllamaLLM:
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.base_url = "http://localhost:11434"

        # Health check
        try:
            requests.get(f"{self.base_url}/api/tags", timeout=2)
            self.enabled = True
            logger.info("Ollama LLM available")
        except Exception:
            self.enabled = False
            logger.warning("Ollama not running")

    def generate(self, prompt: str) -> str:
        if not self.enabled:
            raise RuntimeError("Ollama not available")

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            f"{self.base_url}/api/generate",
            json=payload,
            timeout=300
        )

        response.raise_for_status()
        return response.json()["response"]
