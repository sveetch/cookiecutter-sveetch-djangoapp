.. _factory_boy: https://factoryboy.readthedocs.io/
.. _Flake8: http://flake8.readthedocs.org
.. _freezegun: https://github.com/spulec/freezegun
.. _Pytest: http://pytest.org
.. _pyquery: https://github.com/gawel/pyquery
.. _Tox: http://tox.readthedocs.io

.. _features_quality_intro:

=======
Quality
=======

Quality management is a very important part of development, you should never forget it
and always consider it for each application feature and behavior.

Your application project will have many quality tools already configured but only for
the backend side since frontend is pretty basic.

The included and configured tools are:

* `Pytest`_ with its Django plugin. All tests are written in a specific directory
  ``tests/`` at the root of the repository, you can easily run them all with: ::

    make test

* `factory_boy`_ the companion of Pytest to manage model objects;
* `Flake8`_ to check about PEP8 in your source code (application and tests);
* `pyquery`_ an useful library to parse HTML in your tests. It implements the same
  DOM traversing that jQuery did with the power of lxml;
* `freezegun`_ an useful library to fix datetime in your tests, commonly used with
  code that use things like ``datetime.datetime.now()`` so you can easily test against
  date without to predict or monkey patch them;
* `Tox`_ a powerful tool to launch your quality tasks in various environment. It is
  commonly used to launch your quality task suite before submitting something new and
  ensure it works on everything you support like Python or Django multiple versions;
