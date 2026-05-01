from app.evaluator.runner import Evaluator
from app.utils.loader import load_dataset

def fake_llm(prompt: str) -> str:
    return "Mock response"

def main():
    dataset = load_dataset("datasets/sample_testset.json")
    evaluator = Evaluator(dataset)
    results = evaluator.run(fake_llm)
    evaluator.generate_report(results)

if __name__ == "__main__":
    main()
