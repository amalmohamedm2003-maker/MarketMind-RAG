import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FAISS_INDEX_PATH = os.path.join(
    BASE_DIR, "vectorstore", "faiss_index", "index.faiss"
)

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "auto")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
