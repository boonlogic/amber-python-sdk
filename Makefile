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

test-env-check:
	@if [[ "${AMBER_TEST_LICENSE_FILE}" == "" || "${AMBER_TEST_LICENSE_ID}" == "" ]]; then \
		echo "AMBER_TEST_LICENSE_FILE and AMBER_TEST_LICENSE_ID are required in environment"; \
		exit 1; \
	fi

format-check: format
	git diff --exit-code; if [ $$? -ne 0 ]; then echo "format-check failed"; exit 1; fi; \
	echo "*** format-check passed"

format: docs
	@. local-env/bin/activate && \
	pip install black && \
	black boonamber

docs:
	@. local-env/bin/activate && \
	pdoc3 --force -o docs --template-dir docs --html boonamber

pypi:
	@. local-env/bin/activate && \
	export TWINE_PASSWORD=`python3 bin/get-access-token.py` && \
	python3 -m build && \
	twine upload --skip-existing -u __token__ dist/*

release:
	. ./bin/increment_release.sh && \
	git add pyproject.toml && git commit -m "increment version to $$VERSION" && git push && \
	git tag -a "v$$VERSION" && \
	git push origin --tags


############################
# ========== V1 ========== #
############################

# test-v1, test-v1next, test-dev, test-qa
# run stock profiles from secrets manager
test-% testv1-%:
	@. local-env/bin/activate && \
        cd test && \
	AMBER_TEST_LICENSE_ID=$* coverage run --source=boonamber.v1 -m pytest -x v1/test_client.py && \
	coverage html

# run custom test profile from local file, must have AMBER_TEST_LICENSE_FILE and AMBER_TEST_LICENSE_ID set in env
testv1-local: test-env-check
	@. local-env/bin/activate && \
        cd test && \
	coverage run --source=boonamber.v1 -m pytest -x v1/test_client.py && \
	coverage html

############################
# ========== V2 ========== #
############################

test-local-environment-v2:
	@if [[ "${AMBER_TEST_LICENSE_FILE}" == "" || "${AMBER_V1_LICENSE_ID}" == "" ]]; then \
		echo "AMBER_TEST_LICENSE_FILE and AMBER_V1_LICENSE_ID is required in environment"; \
		exit 1; \
	fi

generate-v2:
	swagger-codegen generate -DmodelTests=false -i amber-api.yml -l python -c swagger-config.json && \
	./bin/clean_comments.sh

testv2-%: test-local-environment-v2
	@. local-env/bin/activate && \
	cd test && \
	AMBER_TEST_LICENSE_ID=$* coverage run --rcfile="../.coveragerc" -m pytest -x v2/test_*.py && \
	coverage html

.PHONY: docs format init test pypi local-env-check test-env-check generate-v2
