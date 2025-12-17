from loguru import logger
from llm.gemini_llm import GeminiRouter

router = GeminiRouter()

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a senior digital marketing strategist.

Context:
{context}

Question:
{question}

Answer clearly and practically.
"""

    logger.info("=== LLM PROMPT START ===")
    logger.info(prompt[:1500])  # avoid log overflow
    logger.info("=== LLM PROMPT END ===")

    try:
        response = router.generate(prompt)
        logger.info(f"Raw LLM response: {response}")

        if response and response.strip():
            return response.strip()

        logger.warning("LLM returned empty text")
        return ""

    except Exception as e:
        logger.exception("LLM generation failed")
        return ""
