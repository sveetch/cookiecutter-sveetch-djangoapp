
=========
Changelog
=========

Version 0.6.0 - Unreleased
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

* TODO: Include basic frontend with last Bootstrap;