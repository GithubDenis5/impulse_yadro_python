import json
import xml.etree.ElementTree as ET


def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def save_json(path: str, data) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_xml(path: str) -> ET.ElementTree:
    return ET.parse(path)


def save_xml(path: str, data: str) -> None:
    with open(path, "w") as f:
        f.write(data)


def min_max_multiplicity(s: str) -> tuple[str, str]:
    t = s.split("..")

    if len(t) == 1:
        return t[0], t[0]

    return t[0], t[1]
