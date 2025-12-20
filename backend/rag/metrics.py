def faithfulness(answer: str, context: str) -> int:
    if not context:
        return 0
    return 1 if any(word in answer for word in context.split()) else 0
