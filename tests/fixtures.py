import pytest

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
