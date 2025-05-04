def calculate_delta(config: dict, patched_config: dict) -> dict:
    additions = [
        {"key": key, "value": value}
        for key, value in patched_config.items()
        if key not in config
    ]

    deletions = [key for key in config.keys() if key not in patched_config]

    updates = [
        {"key": key, "from": config[key], "to": patched_config[key]}
        for key in config.keys() & patched_config.keys()
        if config[key] != patched_config[key]
    ]

    return {"additions": additions, "deletions": deletions, "updates": updates}


def res_config_by_delta(config: dict, delta: dict) -> dict:
    res_patched_config = config.copy()

    for key in delta["deletions"]:
        res_patched_config.pop(key, None)

    for param in delta["additions"]:
        res_patched_config[param["key"]] = param["value"]

    for update in delta["updates"]:
        res_patched_config[update["key"]] = update["to"]

    return res_patched_config
