from xml.etree.ElementTree import ElementTree


def parse_xml(xml_tree: ElementTree) -> tuple[dict, list]:
    root = xml_tree.getroot()
    classes = {}
    aggregation = []

    for el in root:
        if el.tag == "Class":
            class_name = el.get("name")

            attributes = [
                {"name": at.get("name"), "type": at.get("type")}
                for at in el.findall("Attribute")
            ]

            classes[class_name] = {
                "attributes": attributes,
                "documentation": el.get("documentation", ""),
                "isRoot": el.get("isRoot"),
            }
        elif el.tag == "Aggregation":
            aggregation.append(
                {
                    "source": el.get("source"),
                    "target": el.get("target"),
                    "sourceMultiplicity": el.get("sourceMultiplicity"),
                    "targetMultiplicity": el.get("targetMultiplicity"),
                }
            )

    return classes, aggregation
