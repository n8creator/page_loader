install:
	@poetry install

lint:
	poetry run flake8 page_loader

test: lint
	poetry run pytest -v --verbose -s --cov=page_loader tests/

coverage_xml:
	poetry run coverage xml

build:
	poetry build

package-install:
	pip install dist/*.whl
	# pip install --user dist/*.whl

dev-upgrade:
	rm -rf dist/*
	make build
	pip install dist/*.whl --upgrade

loader:
	poetry run page_loader

.PHONY: install lint test coverage_xml build packege_install dev-upgrade loader