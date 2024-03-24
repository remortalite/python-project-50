from gendiff.scripts.gendiff import (add_prefix,
                                     add_prefix_to_dict_keys,
                                     diff_item_sort,
                                     get_dict_sorted,
                                     filter_dict,
                                     generate_diff,
                                     parse_file,
                                     )
from gendiff.scripts import gendiff

from tests.fixtures import (example_json_diff_unsorted,
                            example_json_diff_sorted,
                            example_json_1, example_json_2)

import json


def test_add_prefix():
    assert add_prefix("hello", "+ ") == "+ hello"
    assert add_prefix("hello", "") == "hello"
    assert add_prefix("", "+ ") == "+ "
    assert add_prefix("", "") == "", "Test empty strings"


def test_add_prefix_to_dict_keys():
    dict_ = {"hello": "world", "pi": 3.14}

    assert add_prefix_to_dict_keys(dict_) == {"  hello": "world",
                                              "  pi": 3.14}
    assert add_prefix_to_dict_keys(dict_, "+ ") == {"+ hello": "world",
                                              "+ pi": 3.14}
    assert add_prefix_to_dict_keys(dict_, "- ") == {"- hello": "world",
                                              "- pi": 3.14}
    assert add_prefix_to_dict_keys(dict_, "") == {"hello": "world",
                                              "pi": 3.14}


def test_diff_item_sort():
    item1 = (f"{gendiff.PREFIX_IF_FIRST}hello", 3.14)
    item2 = (f"{gendiff.PREFIX_IF_SECOND}hello", 3.14)

    assert diff_item_sort(item1) == ("hello", 0)
    assert diff_item_sort(item2) == ("hello", 1)


def test_get_dict_sorted(example_json_diff_unsorted,
                         example_json_diff_sorted):
    json_sorted = get_dict_sorted(example_json_diff_unsorted)
    assert json_sorted == example_json_diff_sorted
    assert get_dict_sorted({}) == {}


def test_filter_dict(example_json_diff_sorted):
    assert filter_dict(example_json_diff_sorted, ["  host", "+ timeout"]) == {
            "  host": "hexlet.io", "+ timeout": 20}
    assert filter_dict(example_json_diff_sorted, ["  host"]) == {
            "  host": "hexlet.io"}
    assert filter_dict(example_json_diff_sorted, []) == {}
    assert filter_dict({}, []) == {}
    assert filter_dict({}, ["  host"]) == {}


def test_generate_diff(example_json_diff_sorted):
    result = generate_diff("tests/example/file1.json", "tests/example/file2.json")
    assert example_json_diff_sorted == result


def test_parse_yaml(example_json_1, example_json_2):
    result = parse_file("tests/example/file1.yml")
    assert result == example_json_1
    result = parse_file("tests/example/file2.yaml")
    assert result == example_json_2
