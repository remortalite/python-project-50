lint:
	poetry run flake8 gendiff/

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test-coverage-show:
	poetry run pytest --cov=gendiff --cov-report term-missing
