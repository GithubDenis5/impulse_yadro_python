import json
import xml.etree.ElementTree as ET


def load_json(path: str) -> json:
    with open(path, "r") as f:
        return json.load(f)


def save_json(path: str, data) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_xml(path: str) -> ET:
    return ET.parse(path)


def save_xml(path: str, data: str) -> None:
    with open(path, "w") as f:
        f.write(data)
