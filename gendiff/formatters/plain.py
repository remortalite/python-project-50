def transform_to_str(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif not isinstance(value, str):
        return value
    return f"'{value}'"


def _format_diff(data, *, path=''):
    result = []

    templates_dict = {
        "added":
            "Property '{name}' was added with value: {value}",
        "removed":
            "Property '{name}' was removed",
        "updated":
            "Property '{name}' was updated. From {old_value} to {new_value}"
    }

    for item in data:
        item_string = ""
        state_value = item["state"]

        name = item["name"]

        match state_value:

            case "added":
                item_name = f"{path}.{name}" if path else f"{name}"
                value = transform_to_str(item["value"])
                item_string = templates_dict["added"].format(name=item_name,
                                                             value=value)
                result.append(item_string)

            case "removed":
                item_name = f"{path}.{name}" if path else f"{name}"
                # item_name = _get_name(item["name"], path)
                value = transform_to_str(item["value"])
                temp = templates_dict["removed"]
                item_string = temp.format(name=item_name,
                                          value=value)
                result.append(item_string)

            case "changed":
                item_name = f"{path}.{name}" if path else f"{name}"
                # item_name = _get_name(item["name"], path)
                old_value = transform_to_str(item["value"][0])
                new_value = transform_to_str(item["value"][1])
                temp = templates_dict["updated"]
                item_string = temp.format(name=item_name,
                                          old_value=old_value,
                                          new_value=new_value)
                result.append(item_string)

            case "nested":
                item_name = f"{path}.{name}" if path else f"{name}"
                # item_name = _get_name(item["name"], path)

                result.extend(_format_diff(item["children"],
                                           path=item_name))
    return sorted(result)


def format(data, raw=False):
    prepared_data = _format_diff(data)

    if not prepared_data:
        return data

    if raw:
        return prepared_data

    result_str = ""
    for el in prepared_data:
        if el:
            result_str += f"{el}\n"
    return result_str.rstrip()
