import json
import argparse


def add_prefix(name, prefix):
    return prefix + str(name)


def add_prefix_to_dict_keys(items, prefix="  "):
    new_dict = {}
    for (key, value) in items.items():
        new_dict[add_prefix(key, prefix)] = value
    return new_dict


def diff_item_sort(item):
    tuple_ = (item[0][2:],
              0 if item[0] == '-' else 1)
    return tuple_


def get_dict_sorted(items):
    return dict(sorted(items.items(), key=diff_item_sort))


def gendiff():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    args = parser.parse_args()

    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))

    common_keys = set(file1) & set(file2)
    diff_keys_first = set(file1) - set(file2)
    diff_keys_second = set(file2) - set(file1)

    diff_first = add_prefix_to_dict_keys({k: v for (k, v) in file1.items()
                                          if k in diff_keys_first}, "- ")
    diff_second = add_prefix_to_dict_keys({k: v for (k, v) in file2.items()
                                          if k in diff_keys_second}, "+ ")

    result_dict = diff_first | diff_second

    for key in common_keys:
        if file1[key] == file2[key]:
            result_dict[add_prefix(key, "  ")] = file1[key]
        else:
            result_dict[add_prefix(key, "- ")] = file1[key]
            result_dict[add_prefix(key, "+ ")] = file2[key]

    result_dict = get_dict_sorted(result_dict)
    print(json.dumps(result_dict, indent=4).replace('"', ''))


def main():
    gendiff()


if __name__ == "__main__":
    main()
