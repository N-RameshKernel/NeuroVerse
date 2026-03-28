def quality_score(response: str) -> float:
    score = 0.0

    if len(response.split()) >= 3:
        score += 0.4

    if response.endswith(".") or response.endswith("?"):
        score += 0.3

    verbs = ["is", "was", "are", "means", "called"]
    if any(v in response.lower() for v in verbs):
        score += 0.3

    return round(min(score, 1.0), 3)
