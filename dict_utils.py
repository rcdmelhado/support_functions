def remove_none_values(_dict: dict) -> dict:
    filtered = {}

    for key in _dict:
        if isinstance(_dict[key], dict):
            if remove_none_values(_dict[key]) != {}:
                filtered[key] = remove_none_values(_dict[key])

        elif _dict[key] is not None and _dict[key] != {}:
            filtered[key] = _dict[key]

    return filtered
