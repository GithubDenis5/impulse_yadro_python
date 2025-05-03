from xml_parser import parse_xml
from generators import generate_config_xml, generate_meta_json
from utils.utils import save_xml, save_json, load_json
from config_processor import calculate_delta


def main():
    print("Init")

    classes, aggregations = parse_xml("input/impulse_test_input.xml")

    tree = generate_config_xml(classes, aggregations)
    meta = generate_meta_json(classes, aggregations)

    save_xml("test_out/config.xml", tree)
    save_json("test_out/meta.json", meta)

    config = load_json("input/config.json")
    patched_config = load_json("input/patched_config.json")

    delta = calculate_delta(config, patched_config)

    save_json("test_out/delta.json", delta)


if __name__ == "__main__":
    main()
