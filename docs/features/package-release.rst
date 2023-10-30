.. Attention::

    We are currently working to finish this documentation.

.. _features_releasing_intro:

.. _tox: http://tox.readthedocs.io
.. _twine: https://twine.readthedocs.io

=================
Package releasing
=================

Package configuration has been done in file ``setup.cfg``, we still use the CFG format
instead of TOML because the latter has still some problems in some cases for now.

Release is expected to be on `Python Package Index <https://pypi.org/>`_ (also knowed
as *Pypi*), you will first need to register an account before to be able to publish
anything.

Once a project is released you can grant publishing rights to other trusted users to
collaborate.

Finally, when your release is done, you will have to run the Makefile task ``quality``
to ensure everything is fine and then you can use the task ``release`` that will use
`Twine <https://twine.readthedocs.io/>`_ client to send your package to Pypi. It is
already installed but you will need to create a global configuration.
