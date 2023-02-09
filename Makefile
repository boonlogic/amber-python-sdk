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

# test-v1, test-v1next, test-dev, test-qa
# run stock profiles from secrets manager
test-%:
	@. local-env/bin/activate && \
	cd test && \
	AMBER_TEST_LICENSE_ID=$* coverage run --source=boonamber -m pytest -x test_client.py && \
	coverage html

# run custom test profile from local file, must have AMBER_TEST_LICENSE_FILE and AMBER_TEST_LICENSE_ID set in env
test-local: test-env-check
	@. local-env/bin/activate && \
	cd test && \
	coverage run --source=boonamber -m pytest -x test_client.py && \
	coverage html

# default test target will be against qa
test: test-qa

pypi:
	@. local-env/bin/activate && \
	export TWINE_PASSWORD=`python3 bin/get-access-token.py` && \
	python3 -m build && \
	twine upload --skip-existing -u __token__ dist/*

local-env-check:
	@if [ ! -d ./local-env ]; then \
		echo "must run 'make init' first"; \
		exit 1; \
	fi

docs:
	@. local-env/bin/activate && \
	pdoc3 --force -o docs --html boonamber

test-env-check:
	@if [[ "${AMBER_TEST_LICENSE_FILE}" == "" || "${AMBER_TEST_LICENSE_ID}" == "" ]]; then \
		echo "AMBER_TEST_LICENSE_FILE and AMBER_TEST_LICENSE_ID are required in environment"; \
		exit 1; \
	fi

.PHONY: docs format-check init test pypi local-env-check test-env-check
