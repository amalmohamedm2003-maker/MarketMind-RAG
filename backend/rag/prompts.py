PROMPT_VERSION = "growth_v2"

with open(f"prompts/{PROMPT_VERSION}.txt") as f:
    BASE_PROMPT = f.read()

GROWTH_ANALYSIS_PROMPT = BASE_PROMPT + """

Context:
{context}

Question:
{question}
"""
