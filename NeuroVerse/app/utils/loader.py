import json
def load_dataset(path):
    with open(path) as f:
        return json.load(f)
