PYTHON_INTERPRETER=python3
VENV_PATH=.venv
PYTHON_BIN=$(VENV_PATH)/bin/python
PIP_BIN=$(VENV_PATH)/bin/pip
COOKIECUTTER_BIN=$(VENV_PATH)/bin/cookiecutter

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo
	@echo "  install             -- to install this project with virtualenv and Pip"
	@echo
	@echo "  clean               -- to clean EVERYTHING (Warning)"
	@echo "  clean-pycache       -- to remove all __pycache__, this is recursive from current directory"
	@echo "  clean-install       -- to clean Python side installation"
	@echo
	@echo "  project             -- to create a new project in dist/"
	@echo
	@echo "  flake               -- to launch Flake8 checking"
	@echo "  tests               -- to launch base test suite using Pytest"
	@echo "  quality             -- to launch Flake8 checking and every tests suites"
	@echo

clean-pycache:
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-install:
	@echo ""
	@echo "---> Cleaning install <---"
	@echo ""
	rm -Rf $(VENV_PATH)
.PHONY: clean-install

clean: clean-install clean-pycache
.PHONY: clean

venv:
	@echo ""
	@echo "---> Creating virtual environment <---"
	@echo ""
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# This is required for those ones using old distribution
	$(PIP_BIN) install --upgrade pip
	$(PIP_BIN) install --upgrade setuptools
.PHONY: venv

install: venv
	@echo ""
	@echo "---> Installing <---"
	@echo ""
	$(PIP_BIN) install -r requirements/base.txt
	$(PIP_BIN) install -r requirements/dev.txt
.PHONY: install

project:
	@echo ""
	@echo "---> Creating new project <---"
	@echo ""
	@mkdir -p dist
	$(COOKIECUTTER_BIN) -o dist .
.PHONY: project
