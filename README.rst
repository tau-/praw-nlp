praw-nlp
=======================

|PyPI| |GitHub-license| |Requires.io| |Travis|

    Built from `makenew/python-package <https://github.com/makenew/python-package>`__.n
.. |PyPI| image:: https://img.shields.io/pypi/v/praw-nlp.svg
   :target: https://pypi.python.org/pypi/praw-nlp
   :alt: PyPI
.. |GitHub-license| image:: https://img.shields.io/github/license/tau-/praw-nlp.svg
   :target: ./LICENSE.txt
   :alt: GitHub license
.. |Requires.io| image:: https://img.shields.io/requires/github/tau-/praw-nlp.svg
   :target: https://requires.io/github/tau-/praw-nlp/requirements/
   :alt: Requires.io
.. |Travis| image:: https://img.shields.io/travis/tau-/praw-nlp.svg
   :target: https://travis-ci.org/tau-/praw-nlp
   :alt: Travis

Description
-----------

Scrape Reddit and classify text.

Installation
------------

This package is registered on the `Python Package Index (PyPI)`_
as praw_nlp_.

Add this line to your application's requirements.txt

::

    praw_nlp

and install it with

::

    $ pip install -r requirements.txt

If you are writing a Python package which will depend on this,
add this to your requirements in ``setup.py``.

Alternatively, install it directly using pip with

::

    $ pip install praw_nlp

.. _praw_nlp: https://pypi.python.org/pypi/praw-nlp
.. _Python Package Index (PyPI): https://pypi.python.org/

Development and Testing
-----------------------

Source Code
~~~~~~~~~~~

The `praw-nlp source`_ is hosted on GitHub.
Clone the project with

::

    $ git clone https://github.com/tau-/praw-nlp.git

.. _praw-nlp source: https://github.com/tau-/praw-nlp

Requirements
~~~~~~~~~~~~

You will need `Python 3`_ with pip_.

Install the development dependencies with

::

    $ pip install -r requirements.devel.txt

.. _pip: https://pip.pypa.io/
.. _Python 3: https://www.python.org/

Tests
~~~~~

Lint code with

::

    $ python setup.py lint


Run tests with

::

    $ python setup.py test

Contributing
------------

Please submit and comment on bug reports and feature requests.

To submit a patch:

1. Fork it (https://github.com/tau-/praw-nlp/fork).
2. Create your feature branch (``git checkout -b my-new-feature``).
3. Make changes. Write and run tests.
4. Commit your changes (``git commit -am 'Add some feature'``).
5. Push to the branch (``git push origin my-new-feature``).
6. Create a new Pull Request.

License
-------

This Python package is licensed under the MIT license.

Warranty
--------

This software is provided "as is" and without any express or implied
warranties, including, without limitation, the implied warranties of
merchantibility and fitness for a particular purpose.
