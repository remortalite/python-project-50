from .utils.make_json_diff import make_json_diff

from itertools import chain


JSON_WORDS = {
    True: "true",
    False: "false",
    None: "null"
}

def _format_stylish(data, indent_symbol=" ", indent_size=4, shift_size=2):
    def iter_(current_data, level=1):
        if not isinstance(current_data, dict):
            return f"{current_data}"

        strings = []

        for el in chain(current_data):
            indent = (level * indent_size - shift_size) * indent_symbol
            strings.append(f"{indent}{el}: ")
            if isinstance(current_data[el], dict):
                strings[-1] += "{"
                strings.append(iter_(current_data[el], level + 1))
                strings.append(f"{indent}")
                strings[-1] += shift_size * indent_symbol + "}"
            else:
                if current_data[el] is None or isinstance(current_data[el], bool):
                    strings[-1] += f"{JSON_WORDS[current_data[el]]}"
                else:
                    strings[-1] += f"{current_data[el]}"
        return '\n'.join(strings) if data else data
    return f"{{\n{iter_(data)}\n}}" if data else data


def format(data, raw=False):
    prepared_data = make_json_diff(data)

    return prepared_data if raw else _format_stylish(prepared_data)
