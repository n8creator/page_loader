install:
	@poetry install

lint:
	poetry run flake8 page_loader

test: lint
	# poetry run pytest -v --verbose -s --cov=page_loader tests/

coverage_xml:
	poetry run coverage xml

.PHONY: install lint test coverage_xml