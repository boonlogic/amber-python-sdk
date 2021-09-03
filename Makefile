export SHELL := /bin/bash
export PYTHONPATH := $(shell pwd)

init:
	@python3 -m venv local-env && \
	. local-env/bin/activate && \
	pip3 install --upgrade pip && \
	python3 -m pip install --upgrade setuptools && \
	pip3 install -r requirements.txt && \
	echo "" && \
	echo "virtual environment configured, use 'source local-env/bin/activate' to enable it"

format-check:
	@. local-env/bin/activate && \
	pycodestyle --first boonamber/__init__.py

# test-v1, test-v1next, test-dev, test-qa, test-aoc, test-oap
# add additional .license files in test directory to expand / customize tests
test-%:
	@. local-env/bin/activate && \
	cd test && \
	AMBER_LICENSE_ID=$* coverage run --source=boonamber -m nose -x -verbosity=2 test_client.py && \
	coverage html

# default test target will be against qa
test: test-qa

pypi:
	@. local-env/bin/activate && \
	python3 setup.py sdist && \
	twine upload --skip-existing dist/*

local-env-check:
	@if [ ! -d ./local-env ]; then \
		echo "must run 'make init' first"; \
		exit 1; \
	fi

docs:
	@. local-env/bin/activate && \
	pdoc3 --force -o docs --html boonamber

.PHONY: docs format-check init test pypi local-env-check

