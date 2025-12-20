from transformers import pipeline

print("Loading reasoning LLM (FLAN-T5)...")

llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1
)
def generate_answer(context_docs, question):
    if not context_docs or len(" ".join(context_docs).strip()) < 50:
        return "Insufficient data in knowledge base to answer this question."

    context = "\n".join(context_docs)

    prompt = f"""
You are a senior performance marketing expert.

STRICT RULES:
- Use ONLY the context below
- If the context does not contain an answer, say "Not enough information available"
- Do NOT give generic explanations

Context:
{context}

Question:
{question}

Answer with specific, actionable advice:
"""

    result = llm(
        prompt,
        max_new_tokens=200,
        do_sample=False
    )[0]["generated_text"]

    return result.strip()
