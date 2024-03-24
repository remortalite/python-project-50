import json
import yaml


def parse_file(file_path):
    if file_path.endswith(".json"):
        return json.load(open(file_path))
    elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
        return yaml.safe_load(open(file_path))
    else:
        raise NameError("Wrong file extension! Needs .yaml, .yml or .json")
