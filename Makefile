checkfiles = toy_robot_sim/ tests/
devenv = PYTHONPATH=.

help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    up             Updates dependencies"
	@echo  "    deps           Ensure dependencies are installed"
	@echo  "    lint           Reports all linter violations"
	@echo  "    test           Runs all tests"
	@echo  "    run            Runs the program"

up:
	CUSTOM_COMPILE_COMMAND="make up" pip-compile -U --no-emit-index-url --no-emit-trusted-host requirements.in

deps:
	@pip install --upgrade setuptools
	@pip install -r requirements.txt

pretty:
	isort $(checkfiles)

_lint:
	flake8 $(checkfiles)
	pylint $(checkfiles)

isort:
	isort $(checkfiles)

lint: deps pretty _lint

_test:
	ROLE=test $(devenv) pytest

test: deps _test

run:
	@python toy_robot_sim/cli/cli.py