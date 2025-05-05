from xml_parser import parse_xml
from generators import generate_config_xml, generate_meta_json
from utils.utils import save_xml, save_json, load_json, load_xml
from config_processor import calculate_delta, res_config_by_delta


def main():
    xml_tree = load_xml("input/impulse_test_input.xml")

    classes, aggregations = parse_xml(xml_tree)

    tree = generate_config_xml(classes, aggregations)
    meta = generate_meta_json(classes, aggregations)

    save_xml("out/config.xml", tree)
    save_json("out/meta.json", meta)

    config = load_json("input/config.json")
    patched_config = load_json("input/patched_config.json")

    delta = calculate_delta(config, patched_config)

    save_json("out/delta.json", delta)

    res_patched_config = res_config_by_delta(config, delta)

    save_json("out/res_patched_config.json", res_patched_config)


if __name__ == "__main__":
    main()
