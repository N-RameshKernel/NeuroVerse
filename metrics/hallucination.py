def hallucination_score(response: str, expected: str) -> float:
    response_words = set(response.lower().split())
    expected_words = set(expected.lower().split())

    if not response_words:
        return 1.0

    overlap = response_words.intersection(expected_words)
    hallucination = 1 - (len(overlap) / len(response_words))

    return round(hallucination, 3)
