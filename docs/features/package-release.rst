.. Attention::

    We are currently working to finish this documentation.

.. _Python Package Index: https://pypi.org/
.. _Twine: https://twine.readthedocs.io

.. _features_releasing_intro:

===============
Package release
===============

Package configuration has been done in file ``setup.cfg``, we still use the CFG format
instead of TOML because the latter has still some problems in some cases for now.

Release is expected to be on `Python Package Index`_ (also known as *Pypi*), you will
first need to register an account before to be able to publish anything.

Once a project is released you can grant publishing rights to other trusted users to
collaborate.

Finally, when your release is done, you will have to run the Makefile task ``quality``
to ensure everything is fine and then you can use the task ``release`` that will use
`Twine`_ client to send your package to Pypi. It is
already installed but you will need to create a global configuration.
