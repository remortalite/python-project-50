### Hexlet tests and linter status:
[![Actions Status](https://github.com/remortalite/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/remortalite/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/eba856f6458e29e6a92a/maintainability)](https://codeclimate.com/github/remortalite/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/eba856f6458e29e6a92a/test_coverage)](https://codeclimate.com/github/remortalite/python-project-50/test_coverage)

# Gendiff

Generates differences between two json files.

## Installation

Clone the repository and install using Makefile:

```
git clone https://github.com/remortalite/python-project-50.git

cd python-project-50/

make install build publish package-install
```

## Arguments

Command line format:

```bash
gendiff example/file1.json example/file2.json
```

Usage as python library:
```python3
from gendiff import generate_diff

generate_diff("example/file1.json", "example/file2.json")
```

## Example:

[![asciicast](https://asciinema.org/a/YMZRe6S8quBY44sgtjyFJ1PeW.svg)](https://asciinema.org/a/YMZRe6S8quBY44sgtjyFJ1PeW)
