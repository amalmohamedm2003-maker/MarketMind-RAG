import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "MarketMind AI"
    ENV = os.getenv("ENV", "local")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    MAX_CONTEXT_DOCS = int(os.getenv("MAX_CONTEXT_DOCS", 5))

settings = Settings()
MAX_PROMPT_CHARS = 8000
