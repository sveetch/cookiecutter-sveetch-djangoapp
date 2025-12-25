
=========
Changelog
=========


* Prefix ``[cookie]`` is for changes related to the cookie repository itself (for
  management, documentation, developement, etc..);
* Prefix ``[template]`` is for changes on the application template itself;

Developement
************

* [template] Upgraded frontend to Bootstrap 5.3.8 and minor updates on frontend dev
  stack;
* [template] Upgraded frontend to Bootstrap-icons 1.13.1 and fixed Makefile to properly
  install icons in sandbox;
* [template] Updated frontend 'package.json' command 'css' for a useless
  '--silence-deprecation' argument;
* [template] Pinned sass-embedded to 1.95.1 to remove annoying warning until fixed
  from a more recent Bootstrap version;
* [template] Upgraded frontend engines requirements to Node 22;
* [template] Added support for Python 3.12;
* [template] Added support for Django 6.0 (requires Python>=3.12);
* [template] Upgraded support for DjangoCMS 5.x to version 5.0.5 since it includes
  useful fixes;


Version 0.8.0 - 2025/05/30
**************************

* [template] Removed support for Python<3.10;
* [template] Removed support for Django<4.2;
* [template] Removed support for djangorestframework<3.16.0;
* [template] Removed support for django-cms<5.0.0;
* [template] Removed support for djangocms-text-ckeditor in profit of
  djangocms-text>=0.5.1;
* [template] Updated Tox matrix for tested supports;
* [template] Added dummy ``pyproject.toml`` to fix install with recent Pip and
  Setuptools. This is until template is fully moved to 'pyproject.toml';
* [template] Moved Django manage script from sandbox to template root;
* [template] Added missing setting ``DEFAULT_AUTO_FIELD`` required since Django 4.2;
* [template] Enabled Sphinx extension ``sphinx.ext.todo`` in documentation
  configuration;
* [template] Updated frontend to Bootstrap 5.3.6 and sass-embedded;
* [template] Updated CMS settings for DjangoCMS>=4;
* [template] Updated CMS plugin tests to correctly work with DjangoCMS>=4;
* [template] Added support for optionnal djangocms-versioning;


Version 0.7.2 - 2024/09/18
**************************

* [cookie] Minor change to upgrade cookie documentation requirements;
* [cookie] Adopted Tox for quality control on project generation instead of the shell
  script ``check-all-variant.sh``;
* [cookie] Removed deprecated ``check-all-variant.sh``;
* [cookie] Added ``compat`` module with some compatibility wrappers (currently with
  default storage class and ZoneInfo);
* [cookie] Fixed Makefile task ``project`` that was using a wrong cookie path;
* [cookie] Fixed tests that were using removed Pytz in profit of ZoneInfo;
* [cookie] Updated documentation;
* [template] Updated included script ``freezer.py`` to use ``importlib.metadata``
  instead of deprecated ``pkg_resources``;
* [template] Updated ``MANIFEST.in``;


Version 0.7.1 - 2024/09/11
**************************

* [cookie] Added missing credits for SVG repo;
* [template] Changed Pytest configuration so it adopts cleaner options for verbosity
  output;
* [template] Removed support for Python<3.9;
* [template] Removed support for Django<4.2;
* [template] Added support for Python from 3.9 to 3.11;
* [template] Added support for Django>=5.0;
* [template] Pinned various requirement to a minimal version to speed up Pip install;
* [template] Pinned DjangoCMS below 4.0 since we don't support this major release yet;
* [template] Fixed application description in its ``__init__.py`` that was using an
  hardcoded text from another existing project instead of cookiecutter variable,
  close issue #15;
* [template] Fixed 'frontend' Makefile cleaning tasks that were not conditionnated to
  frontend option, close issue #14;


Version 0.7.0 - 2023/10/30
**************************

This is a major upgrade to add DjangoCMS plugin option, improve quality and
documentation.

* [cookie] Added documentation;
* [cookie] Added a new option ``include_cmsplugin`` to include a minimal DjangoCMS
  plugin with basic test coverage. This option also involves changes on sandbox to
  include required DjangoCMS configuration and requirements;
* [cookie] Added Bash script ``check-all-variant.sh`` that can run a suite of template
  variants to build and run quality task, this a kind of Tox for the template;
* [cookie] Added Python script ``docs/makefile_parser.py`` to automatize Makefile help
  texts documentation;
* [template] Fixed package setup that didn't defined keywords with comma separation;
* [template] Fixed base setting ``TEMPLATES`` to use ``Path`` instead of
  ``os.path.join``;
* [template] Documentation settings has been moved into sandbox settings modules so it
  is more simple to manage;
* [template] Added compatibility fix with Django>=4.2 for ``USE_L10N`` in settings to
  avoid warning;
* [template] Moved ``tests.utils`` to ``{{cookiecutter.app_name}}.utils.tests``;
* [template] Improved References documentation;
* [template] Added Makefile tasks ``po`` and ``mo``;


Version 0.6.0 - 2023/10/20
**************************

This is a major upgrade to improve quality, documentation and package.

* [cookie] Started this history changelog;
* [cookie] Added ``_sveetch_djangoapp_version`` variable to
  ``cookiecutter.json`` for versioning template;
* [cookie] Upgraded to ``cookiecutter>=2.3.0``;
* [cookie] Added Makefile task ``project`` to create projects in ``dist/``;
* [cookie] Added a new option ``init_git_repository`` to enabled for automatic GIT
  repository initialization on created project;
* [cookie] Renamed option ``enable_drf`` to ``include_api``;
* [cookie] Added a post hook to manage CLI files removing and GIT initialization
  depending options;
* [template] Updated ``.readthedocs.yml`` file to follow service deprecations changes;
* [template] Upgraded documentation to Furo theme, improved sphinx_reload script and
  moved it into ``docs/``;
* [template] Improved Makefile (better variable names and sections);
* [template] Included README in ``docs/index.rst`` instead of managing the same content
  twice;
* [template] Don't test all supported Python and Django versions in Tox config, only
  the min and max ones;
* [template] Fixed ``exceptions.py`` to define class names named from package instead
  of dummy ``MyApp``;
* [template] Added new option ``include_frontend`` to include a basic frontend with
  Bootstrap 5.3.2;
