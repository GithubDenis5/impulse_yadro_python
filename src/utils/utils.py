import json


def load_json(path: str) -> json:
    with open(path, "r") as f:
        return json.load(f)


def save_json(path: str, data: json) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
