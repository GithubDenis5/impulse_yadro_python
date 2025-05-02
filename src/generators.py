from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom as md


def generate_config_xml(classes: dict, aggregations: list):
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

    # return tostring(root, "unicode", short_empty_elements=False)

    bad_xml_string = tostring(root, "unicode", short_empty_elements=False)

    formated_xml_string = md.parseString(bad_xml_string).toprettyxml(indent="\t")

    return formated_xml_string
