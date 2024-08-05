export SHELL := /bin/bash
export PYTHONPATH := $(shell pwd)

init: ## initialize python package
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

examples-env-check:
	@if [[ "${AMBER_LICENSE_FILE}" == "" ]]; then \
		echo "AMBER_LICENSE_FILE is required in environment"; \
		exit 1; \
	fi

list-test-env: ## list available test environments
	@aws secretsmanager get-secret-value --secret amber-test-users | jq -rc '.SecretString'

format-check: format ## check for valid code formatting
	git diff --exit-code; if [ $$? -ne 0 ]; then echo "format-check failed"; exit 1; fi; \
	echo "*** format-check passed ***"

format: docs ## format all boonamber code
	@. local-env/bin/activate && \
	pip install black && \
	black boonamber

docs: ## generate documentation
	@. local-env/bin/activate && \
	pdoc3 --force -o docs --template-dir docs --html boonamber

release: ## generate another release for amber-python-sdk
	. ./bin/increment_release.sh && \
	git add pyproject.toml && git commit -m "increment version to $$VERSION" && git push && \
	git tag -a "v$$VERSION" && \
	git push origin --tags


############################
# ========== V1 ========== #
############################

# test-v1, test-v1next, test-dev, test-qa
# run stock profiles from secrets manager
test-% testv1-%: ## run amber v1 tests (see % values via make list-test-env)
	@. local-env/bin/activate && \
        cd test && \
	AMBER_TEST_LICENSE_ID=$* coverage run --source=boonamber.v1 -m pytest -x v1/test_client.py && \
	coverage html

examplesv1-%: ## run all amber v1 example programs
	@. local-env/bin/activate; \
	cd examples/v1 && \
	for f in *.py; do \
		AMBER_LICENSE_ID=$* python $${f} \
		|| exit 1; \
	done

############################
# ========== V2 ========== #
############################

generate-v2: ## generate new code for v2 python models using swagger spec
	swagger-codegen generate -DmodelTests=false -i amber-api.yml -l python -c swagger-config.json && \
	./bin/clean_comments.sh

testv2-%: ## run amber-v2 tests (see % values with make list-test-env)
	@. local-env/bin/activate && \
	cd test && \
	AMBER_TEST_LICENSE_ID=$* coverage run --rcfile="../.coveragerc" -m pytest -x v2/test_*.py && \
	coverage html

examplesv2-%: ## run all amber v2 example programs
	@. local-env/bin/activate; \
	cd examples/v2 && \
	for f in *.py; do \
		AMBER_V2_LICENSE_ID=$* python $${f} \
		|| exit 1; \
	done

help: ## Display this help screen
	@grep -h -E '^[A-Za-z].*:.* ## ' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: docs format init test pypi local-env-check test-env-check generate-v2
