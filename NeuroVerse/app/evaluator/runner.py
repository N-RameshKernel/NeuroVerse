from app.metrics.faithfulness import check_faithfulness
from app.metrics.hallucination import detect_hallucination
from app.metrics.quality import score_quality

class Evaluator:
    def __init__(self, dataset):
        self.dataset = dataset

    def run(self, llm_func):
        results = []
        for item in self.dataset:
            response = llm_func(item["question"])
            results.append({
                "question": item["question"],
                "response": response,
                "faithfulness": check_faithfulness(response, item["expected_answer"]),
                "hallucination": detect_hallucination(response),
                "quality": score_quality(response)
            })
        return results

    def generate_report(self, results):
        for r in results:
            print(r)
