.. _Bootstrap frontend toolkit: https://getbootstrap.com/
.. _Webpack: https://webpack.js.org/
.. _Node.js: https://nodejs.org
.. _ITCSS: https://stackoverflow.com/tags/itcss/info
.. _Sass: https://sass-lang.com/documentation/
.. _Webpack: https://webpack.js.org/

.. _features_frontend_intro:

========
Frontend
========

.. Note::
    This is an optional feature during creation of application project. It will only be
    available if you enabled it.

This will configures a basic modern frontend with a `Node.js`_ environment,
`Bootstrap frontend toolkit`_ and `Webpack`_.

The included frontend layout is pretty basic and it just fully enables Bootstrap with
default configuration.

Layout CSS is built from `Sass`_, the Sass sources structure has been made to
follow `ITCSS`_ concept.

Frontend JavaScript only enable all Bootstrap components and you may also enable jQuery
if needed.

Finally, `Webpack`_ is used to build asset bundles without the need of dummy HTML file
to define assets to build, everything bundle to manage is clearly defined in Webpack
configuration.

.. Hint::
    Included frontend goal is mainly for the demonstration sandbox because commonly
    you should not attach your application to a specific a frontend toolkit. Application
    users should be free to use any other toolkit.
