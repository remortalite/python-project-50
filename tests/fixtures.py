import pytest

import json


@pytest.fixture
def example_json_diff_unsorted():
    return json.loads("""{
  "+ timeout": 20,
  "- follow": false,
  "+ verbose": true,
  "  host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "- timeout": 50}""")


@pytest.fixture
def example_json_diff_sorted():
    return json.loads("""{
  "- follow": false,
  "  host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "- timeout": 50,
  "+ timeout": 20,
  "+ verbose": true}""")


@pytest.fixture
def example_json_1():
    return json.loads(open("tests/example/file1.json").read())


@pytest.fixture
def example_json_2():
    return json.loads(open("tests/example/file2.json").read())
