from xml_parser import parse_xml
from generators import generate_config_xml
from utils.utils import save_xml


def main():
    print("Init")

    classes, aggregations = parse_xml("input/impulse_test_input.xml")

    tree = generate_config_xml(classes, aggregations)

    save_xml("config.xml", tree)


if __name__ == "__main__":
    main()
