def calculate_delta(config, patched_config):
    additions = [
        {"key": key, "value": value}
        for key, value in patched_config.items()
        if key not in config
    ]

    deletions = [key for key in patched_config.items() if not (key in config)]

    updates = [
        {"key": key, "from": config[key], "to": patched_config[key]}
        for key in config.keys() & patched_config.keys()
        if config[key] != patched_config[key]
    ]

    return {"additions": additions, "deletions": deletions, "updates": updates}
