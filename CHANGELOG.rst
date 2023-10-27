
=========
Changelog
=========

Version 0.7.0 - Unreleased
--------------------------

* Fixed package setup that didn't defined keywords with comma separation;
* Fixed base setting ``TEMPLATES`` to use ``Path`` instead of ``os.path.join``;
* Documentation settings has been moved into sandbox settings modules so it is more
  simple to manage;
* Added compatibility fix with Django>=4.2 for ``USE_L10N`` in settings to avoid
  warning;

TODO
....

* Add optional DjangoCMS plugin;

  - [x] Add DjangoCMS config;
  - [x] Fixed tests for variance with or without DjangoCMS;
  - [x] Add files removing from posthook for when "include plugin" option is disabled;
  - [x] Add basic plugin;
  - [x] Add minimal tests for plugin;
  - [ ] Move tests.utils in {application}/utils/..

* Documentation build on RTD has to be tested since doc settings change and this will
  need to done on a generated project, so in this cookie sample repo with pre branch
  to activate etc..;
* Add option to use absolute path instead relative path for package module importations
  (absolute path ease to include module into an existing project);
* Add Makefile tasks for PO and MO?


Version 0.6.0 - 2023/10/20
--------------------------

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
