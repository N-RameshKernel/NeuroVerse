def generate_report(results):
    print("\n========== LLM BENCHMARK REPORT ==========")

    for i, item in enumerate(results):
        print(f"\n✅ Test Case {i+1}")
        print("Prompt   :", item["prompt"])
        print("Expected :", item["expected"])
        print("Response :", item["response"])

        print("\n📊 Scores:")
        for metric, score in item["metrics"].items():
            print(f"  • {metric.title():15}: {score}")

        print("-" * 50)

    print("\n✅ Completed Evaluation Successfully!\n")
