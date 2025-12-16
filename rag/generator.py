from llm.gemini_llm import GeminiRouter
from rag.prompts import GROWTH_ANALYSIS_PROMPT

router = GeminiRouter()

def generate_answer(context, question):
    prompt = GROWTH_ANALYSIS_PROMPT.format(
        context=context,
        question=question
    )
    return router.generate(prompt)
