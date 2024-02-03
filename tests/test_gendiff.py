from gendiff.scripts.gendiff import (add_prefix,
                                     add_prefix_to_dict_keys,
                                     diff_item_sort,
                                     get_dict_sorted,
                                     filter_dict,
                                     generate_diff,
                                     )
from gendiff.scripts import gendiff

import pytest


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


import json

@pytest.fixture
def example_json():
    return json.loads("""{
  "+ timeout": 20,
  "- follow": false,
  "+ verbose": true,
  "  host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "- timeout": 50}""")

@pytest.fixture
def example_file1():
    return json.loads("""{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false}""")


@pytest.fixture
def example_file2():
    return json.loads("""{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"}""")


def test_get_dict_sorted(example_json):
    d_ = get_dict_sorted(example_json)
    answer = json.loads("""{
  "- follow": false,
  "  host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "- timeout": 50,
  "+ timeout": 20,
  "+ verbose": true}""")
    assert d_ == answer
    assert get_dict_sorted({}) == {}


def test_filter_dict(example_json):
    assert filter_dict(example_json, ["  host", "+ timeout"]) == {
            "  host": "hexlet.io", "+ timeout": 20}
    assert filter_dict(example_json, ["  host"]) == {
            "  host": "hexlet.io"}
    assert filter_dict(example_json, []) == {}
    assert filter_dict({}, []) == {}
    assert filter_dict({}, ["  host"]) == {}


def test_generate_diff(example_file1, example_file2, example_json):
    result = get_dict_sorted(example_json)

    assert generate_diff("example/file1.json", "example/file2.json") == result
