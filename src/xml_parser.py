from utils.utils import load_xml


def parse_xml(path: str) -> dict:
    xml_tree = load_xml(path)
    root = xml_tree.getroot()
    classes = {}

    for el in root:
        if el.tag == "Class":
            class_name = el.get("name")

            attributes = [
                {"name": at.get("name"), "type": at.get("type")}
                for at in el.findall("Attribute")
            ]

            classes[class_name] = {
                "attributes": attributes,
                "documentation": el.get("documentation"),
                "isRoot": el.get("isRoot"),
            }

    return classes
