def faithfulness_score(response: str, context: str) -> float:
    response_words = set(response.lower().split())
    context_words = set(context.lower().split())

    if not response_words:
        return 0.0

    overlap = response_words.intersection(context_words)
    faithfulness = len(overlap) / len(response_words)

    return round(faithfulness, 3)
