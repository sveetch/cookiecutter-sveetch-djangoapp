PYTHON_INTERPRETER=python3
VENV_PATH=.venv

PYTHON_BIN=$(VENV_PATH)/bin/python
PIP_BIN=$(VENV_PATH)/bin/pip
FLAKE_BIN=$(VENV_PATH)/bin/flake8
PYTEST_BIN=$(VENV_PATH)/bin/pytest
COOKIECUTTER_BIN=$(VENV_PATH)/bin/cookiecutter
SPHINX_RELOAD_BIN=$(PYTHON_BIN) docs/sphinx_reload.py
MAKEFILE_PARSER_BIN=$(PYTHON_BIN) docs/makefile_parser.py

# Formatting variables, FORMATRESET is always to be used last to close formatting
FORMATBLUE:=$(shell tput setab 4)
FORMATBOLD:=$(shell tput bold)
FORMATRESET:=$(shell tput sgr0)

help:
	@echo "Please use 'make <target> [<target>...]' where <target> is one of"
	@echo
	@echo "  Cleaning"
	@echo "  ========"
	@echo
	@echo "  clean               -- to clean EVERYTHING (Warning)"
	@echo "  clean-pycache       -- to remove all __pycache__, this is recursive from current directory"
	@echo "  clean-install       -- to clean Python side installation"
	@echo "  clean-doc           -- to remove documentation builds"
	@echo "  clean-dist          -- to remove distributed directory"
	@echo
	@echo "  Installation"
	@echo "  ============"
	@echo
	@echo "  install             -- to install this project with virtualenv and Pip"
	@echo
	@echo "  Usage"
	@echo "  ====="
	@echo
	@echo "  project              -- to create a new project"
	@echo
	@echo "  Documentation"
	@echo "  ============="
	@echo
	@echo "  docs                 -- to build documentation"
	@echo "  livedocs             -- to run livereload server to rebuild documentation on source changes"
	@echo
	@echo "  Quality"
	@echo "  ======="
	@echo
	@echo "  flake8               -- to check codestyle on cookie internals"
	@echo "  template-flake8      -- to check codestyle on project template (it is expected to fail because of Jinja syntax in some files)"
	@echo

clean-pycache:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear Python cache <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-install:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear installation <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(VENV_PATH)
.PHONY: clean-install

clean-doc:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear documentation <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf docs/_build
.PHONY: clean-doc

clean-dist:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning distributed directory <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf dist
.PHONY: clean-dist

clean: clean-install clean-doc clean-pycache
.PHONY: clean

venv:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Install virtual environment <---$(FORMATRESET)\n"
	@echo ""
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# Uncomment these two lines if you want development install support on old
	# distributions (<2020)
	#$(PIP_BIN) install --upgrade pip
	#$(PIP_BIN) install --upgrade setuptools
.PHONY: venv

install: venv
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Install everything for development <---$(FORMATRESET)\n"
	@echo ""
	$(PIP_BIN) install -r requirements/dev.txt -r requirements/docs-live.txt
.PHONY: install

docs:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building documentation <---$(FORMATRESET)\n"
	@echo ""
	$(MAKEFILE_PARSER_BIN) "{{cookiecutter.package_name}}/Makefile" --format rst --destination docs/_static/makefile_help.rst
	cd docs && make html
.PHONY: docs

livedocs:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Watching documentation sources <---$(FORMATRESET)\n"
	@echo ""
	$(SPHINX_RELOAD_BIN)
.PHONY: livedocs

project:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Creating new project <---$(FORMATRESET)\n"
	@echo ""
	@mkdir -p dist
	@$(COOKIECUTTER_BIN) -o dist .
.PHONY: project

flake8:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Checking codestyle on cookie internals <---$(FORMATRESET)\n"
	@echo ""
	@$(FLAKE_BIN) --statistics --show-source hooks
.PHONY: flake8

template-flake8:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Checking codestyle on project template <---$(FORMATRESET)\n"
	@echo ""
	@$(FLAKE_BIN) --statistics --show-source \{\{\cookiecutter.project_name\}\}
.PHONY: template-flake8
