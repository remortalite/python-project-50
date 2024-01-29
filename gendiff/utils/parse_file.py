import json


def parse_file(path):
    if not path:
        raise ValueError("Path name cannot be empty!")
    lines = json.load(open(path))
    return lines
