from evaluator.runner import LLMEvaluator
from evaluator.report import generate_report


def fake_llm(prompt: str):
    knowledge = {
        "capital of France": "The capital of France is Paris.",
        "discovered gravity": "Gravity was discovered by Isaac Newton.",
        "largest planet": "The largest planet is Jupiter."
    }

    for key in knowledge:
        if key in prompt.lower():
            return knowledge[key]

    return "I don't know."


if __name__ == "__main__":
    print("\n🚀 Starting LLM Evaluation Framework...\n")

    evaluator = LLMEvaluator("datasets/sample_testset.json")
    results = evaluator.run(fake_llm)

    generate_report(results)
