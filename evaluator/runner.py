from metrics.hallucination import hallucination_score
from metrics.faithfulness import faithfulness_score
from metrics.quality import quality_score
from utils.loader import load_json_dataset


class LLMEvaluator:
    def __init__(self, dataset_path: str):
        self.test_cases = load_json_dataset(dataset_path)

    def evaluate_response(self, response: str, expected: str, context: str):
        return {
            "hallucination": hallucination_score(response, expected),
            "faithfulness": faithfulness_score(response, context),
            "quality": quality_score(response)
        }

    def run(self, model_function):
        results = []

        for case in self.test_cases:
            prompt = case["prompt"]
            expected = case["expected_answer"]
            context = case["context"]

            response = model_function(prompt)
            metrics = self.evaluate_response(response, expected, context)

            results.append({
                "prompt": prompt,
                "expected": expected,
                "response": response,
                "metrics": metrics
            })

        return results
