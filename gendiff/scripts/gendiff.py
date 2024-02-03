import json
import argparse


PREFIX_IF_FIRST = "- "
PREFIX_IF_SECOND = "+ "
PREFIX_IF_SAME = "  "


def add_prefix(name, prefix):
    return prefix + str(name)


def add_prefix_to_dict_keys(items, prefix=PREFIX_IF_SAME):
    new_dict = {}
    for (key, value) in items.items():
        new_dict[add_prefix(key, prefix)] = value
    return new_dict


def diff_item_sort(item):
    tuple_ = (item[0][2:],
              0 if item[0].startswith(PREFIX_IF_FIRST) else 1)
    return tuple_


def get_dict_sorted(items):
    return dict(sorted(items.items(), key=diff_item_sort))


def filter_dict(items, keys_include):
    return {k: v for (k, v) in items.items() if k in keys_include}


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    common_keys = set(file1) & set(file2)
    diff_keys_first = set(file1) - set(file2)
    diff_keys_second = set(file2) - set(file1)

    diff_first = add_prefix_to_dict_keys(filter_dict(file1, diff_keys_first),
                                         PREFIX_IF_FIRST)
    diff_second = add_prefix_to_dict_keys(filter_dict(file2, diff_keys_second),
                                          PREFIX_IF_SECOND)

    result_dict = diff_first | diff_second

    for key in common_keys:
        if file1[key] == file2[key]:
            result_dict[add_prefix(key, PREFIX_IF_SAME)] = file1[key]
        else:
            result_dict[add_prefix(key, PREFIX_IF_FIRST)] = file1[key]
            result_dict[add_prefix(key, PREFIX_IF_SECOND)] = file2[key]

    result_dict = get_dict_sorted(result_dict)
    return result_dict


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    args = parser.parse_args()

    result = generate_diff(args.first_file, args.second_file)
    print(json.dumps(result, indent=4).replace('"', ''))


if __name__ == "__main__":
    main()
