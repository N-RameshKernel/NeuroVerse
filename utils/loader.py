import json

def load_json_dataset(path: str):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
