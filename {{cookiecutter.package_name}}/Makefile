PYTHON_INTERPRETER=python3
VENV_PATH=.venv

FRONTEND_DIR=frontend
SANDBOX_DIR=sandbox
STATICFILES_DIR=$(SANDBOX_DIR)/static-sources

PYTHON_BIN=$(VENV_PATH)/bin/python
PIP_BIN=$(VENV_PATH)/bin/pip
FLAKE_BIN=$(VENV_PATH)/bin/flake8
PYTEST_BIN=$(VENV_PATH)/bin/pytest
SPHINX_RELOAD_BIN=$(PYTHON_BIN) docs/sphinx_reload.py
TOX_BIN=$(VENV_PATH)/bin/tox
TWINE_BIN=$(VENV_PATH)/bin/twine

DJANGO_MANAGE=$(SANDBOX_DIR)/manage.py

PACKAGE_NAME={{ cookiecutter.package_name }}
PACKAGE_SLUG={{ cookiecutter.package_name.replace('-', '_') }}
APPLICATION_NAME={{ cookiecutter.app_name }}

# Formatting variables, FORMATRESET is always to be used last to close formatting
FORMATBLUE:=$(shell tput setab 4)
FORMATGREEN:=$(shell tput setab 2)
FORMATRED:=$(shell tput setab 1)
FORMATBOLD:=$(shell tput bold)
FORMATRESET:=$(shell tput sgr0)

help:
	@echo "Please use 'make <target> [<target>...]' where <target> is one of"
	@echo
	@echo "  Cleaning"
	@echo "  ========"
	@echo
	@echo "  clean                      -- to clean EVERYTHING (Warning)"
	@echo "  clean-var                  -- to clean data (uploaded medias, database, etc..)"
	@echo "  clean-doc                  -- to remove documentation builds"
	@echo "  clean-install              -- to clean Python side installation"
	@echo "  clean-pycache              -- to recursively remove all Python cache files"
	@echo
	@echo "  Documentation"
	@echo "  ============="
	@echo
	@echo "  docs                       -- to build documentation"
	@echo "  livedocs                   -- to run a 'live reloaded' server for documentation"
	@echo
	@echo "  Installation"
	@echo "  ============"
	@echo
	@echo "  freeze-dependencies        -- to write installed dependencies versions in frozen.txt"
	@echo "  install                    -- to install this project with virtualenv and Pip"
	@echo
	@echo "  Django commands"
	@echo "  ==============="
	@echo
	@echo "  run                        -- to run Django development server"
	@echo "  check-migrations           -- to check for pending application migrations (do not write anything)"
	@echo "  migrations                 -- to create new migrations for application after changes"
	@echo "  migrate                    -- to apply demo database migrations"
	@echo "  superuser                  -- to create a superuser for Django admin"
	@echo
	@echo "  Quality"
	@echo "  ======="
	@echo
	@echo "  check-release              -- to check package release before uploading it to PyPi"
	@echo "  flake                      -- to launch Flake8 checking"
	@echo "  quality                    -- to launch run quality tasks and checks"
	@echo "  test                       -- to launch base test suite using Pytest"
	@echo "  test-initial               -- to launch base test suite using Pytest and re-initialized database"
	@echo "  tox                        -- to launch tests for every Tox environments"
	@echo
	@echo "  Release"
	@echo "  ======="
	@echo
	@echo "  release                    -- to release latest package version on PyPi"
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
	rm -Rf $(PACKAGE_SLUG).egg-info
.PHONY: clean-install

clean-doc:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear documentation <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf docs/_build
.PHONY: clean-doc

clean-var:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear 'var/' directory <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf var
.PHONY: clean-var

clean: clean-var clean-doc clean-install clean-pycache
.PHONY: clean

create-var-dirs:
	@mkdir -p var/db
	@mkdir -p var/static/css
	@mkdir -p var/media
	@mkdir -p $(SANDBOX_DIR)/media
	@mkdir -p $(STATICFILES_DIR)/css
.PHONY: create-var-dirs

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

install-backend:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Install everything for development <---$(FORMATRESET)\n"
	@echo ""
	$(PIP_BIN) install -e .[dev,quality,doc,doc-live,release]
.PHONY: install-backend

install-frontend:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Installing frontend requirements <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm install
# 	@mkdir -p $(STATICFILES_DIR)/fonts
# 	${MAKE} icon-font
.PHONY: install-frontend


install: venv create-var-dirs install-backend migrate
# install-frontend frontend
.PHONY: install

check-django:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running Django System check <---$(FORMATRESET)\n"
	@echo ""
	$(PYTHON_BIN) $(DJANGO_MANAGE) check
.PHONY: check-django

migrations:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Making application migrations <---$(FORMATRESET)\n"
	@echo ""
	$(PYTHON_BIN) $(DJANGO_MANAGE) makemigrations $(APPLICATION_NAME)
.PHONY: migrations

check-migrations:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Checking for pending backend model migrations <---$(FORMATRESET)\n"
	@echo ""
	$(PYTHON_BIN) $(DJANGO_MANAGE) makemigrations --check --dry-run -v 3 $(APPLICATION_NAME)
.PHONY: check-migrations

migrate:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Apply pending migrations <---$(FORMATRESET)\n"
	@echo ""
	$(PYTHON_BIN) $(DJANGO_MANAGE) migrate
.PHONY: migrate

superuser:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Create new superuser <---$(FORMATRESET)\n"
	@echo ""
	$(PYTHON_BIN) $(DJANGO_MANAGE) createsuperuser
.PHONY: superuser

run:
	@echo ""
	@echo "==== Running development server ===="
	@echo ""
	$(PYTHON_BIN) $(DJANGO_MANAGE) runserver 0.0.0.0:8001
.PHONY: run

css:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building CSS for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run-script css
.PHONY: css

watch-sass:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Watching Sass sources for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run-script watch-css
.PHONY: watch-sass

css-prod:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building CSS for production environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run-script css-prod
.PHONY: css-prod

js:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building distributed Javascript for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run js
.PHONY: js

watch-js:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Watching Javascript sources for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run watch-js
.PHONY: watch-js

js-prod:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building distributed Javascript for production environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run js-prod
.PHONY: js-prod

frontend: css js
.PHONY: frontend

frontend-prod: css-prod js-prod
.PHONY: frontend-prod

docs:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build documentation <---$(FORMATRESET)\n"
	@echo ""
	cd docs && make html
.PHONY: docs

livedocs:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Watching documentation sources <---$(FORMATRESET)\n"
	@echo ""
	$(SPHINX_RELOAD_BIN)
.PHONY: livedocs

flake:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Flake <---$(FORMATRESET)\n"
	@echo ""
	$(FLAKE_BIN) --statistics --show-source $(APPLICATION_NAME) tests
.PHONY: flake

test:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Tests <---$(FORMATRESET)\n"
	@echo ""
	$(PYTEST_BIN) -vv tests/
	rm -Rf var/media-tests/
.PHONY: test

test-initial:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Tests from zero <---$(FORMATRESET)\n"
	@echo ""
	$(PYTEST_BIN) -vv --reuse-db --create-db tests/
	rm -Rf var/media-tests/
.PHONY: test-initial

freeze-dependencies:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Freeze dependencies versions <---$(FORMATRESET)\n"
	@echo ""
	$(VENV_PATH)/bin/python freezer.py
.PHONY: freeze-dependencies

build-package:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build package <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf dist
	$(VENV_PATH)/bin/python setup.py sdist
.PHONY: build-package

release: build-package
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Release package <---$(FORMATRESET)\n"
	@echo ""
	$(TWINE_BIN) upload dist/*
.PHONY: release

check-release: build-package
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Check package <---$(FORMATRESET)\n"
	@echo ""
	$(TWINE_BIN) check dist/*
.PHONY: check-release

tox:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Launch all Tox environments <---$(FORMATRESET)\n"
	@echo ""
	$(TOX_BIN)
.PHONY: tox

quality: test-initial flake check-migrations docs check-release freeze-dependencies
	@echo ""
	@printf "$(FORMATGREEN)$(FORMATBOLD) ♥ ♥ Everything should be fine ♥ ♥ $(FORMATRESET)\n"
	@echo ""
	@echo ""
.PHONY: quality
