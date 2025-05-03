from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom as md

from utils.utils import min_max_multiplicity


def generate_config_xml(classes: dict, aggregations: list) -> str:
    root_name = next(name for name, data in classes.items() if data["isRoot"] == "true")
    root = Element(root_name)

    def build_class_tree(parent: Element, class_name: Element):
        for att in classes[class_name]["attributes"]:
            element = SubElement(parent, att["name"])
            element.text = att["type"]

        for agg in aggregations:
            if agg["target"] == class_name:
                child = agg["source"]
                child_element = SubElement(parent, child)
                build_class_tree(child_element, child)

    build_class_tree(root, root_name)

    bad_xml_string = tostring(root, "unicode", short_empty_elements=False)

    formated_xml_string = md.parseString(bad_xml_string).toprettyxml(indent="\t")

    return formated_xml_string


def generate_meta_json(classes: dict, aggregations: list) -> list:
    meta = []

    for name, data in classes.items():
        parameters = [
            {"name": att["name"], "type": att["type"]} for att in data["attributes"]
        ]

        for agg in aggregations:
            if agg["target"] == name:
                parameters.append(
                    {
                        "name": agg["source"],
                        "type": "class",
                    }
                )

        class_meta = {
            "class": name,
            "documentation": data["documentation"],
            "isRoot": data["isRoot"],
        }

        if data["isRoot"] != "true":
            min_mult, max_mult = "", ""
            for agg in aggregations:
                if agg["source"] == name:
                    min_mult, max_mult = min_max_multiplicity(agg["sourceMultiplicity"])

            class_meta["max"] = max_mult
            class_meta["min"] = min_mult

        class_meta["parameters"] = parameters

        meta.append(class_meta)

    return meta
