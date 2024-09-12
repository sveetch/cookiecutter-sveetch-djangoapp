
=========
Changelog
=========


* Prefix ``[cookie]`` is for changes related to the cookie repository itself (for
  management, documentation, developement, etc..);
* Prefix ``[template]`` is for changes on the application template itself;


Unreleased developement
-----------------------

* [cookie] Minor change to upgrade cookie documentation requirements;
* [cookie] Adopted Tox for quality control on project generation instead of the shell
  script ``check-all-variant.sh``;


Version 0.7.1 - 2024/09/11
--------------------------

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
--------------------------

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
