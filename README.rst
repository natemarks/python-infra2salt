========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-infra2salt/badge/?style=flat
    :target: https://readthedocs.org/projects/python-infra2salt
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/natemarks/python-infra2salt.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/natemarks/python-infra2salt

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/natemarks/python-infra2salt?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/natemarks/python-infra2salt

.. |requires| image:: https://requires.io/github/natemarks/python-infra2salt/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/natemarks/python-infra2salt/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/natemarks/python-infra2salt/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/natemarks/python-infra2salt

.. |version| image:: https://img.shields.io/pypi/v/infra2salt.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/infra2salt

.. |commits-since| image:: https://img.shields.io/github/commits-since/natemarks/python-infra2salt/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/natemarks/python-infra2salt/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/infra2salt.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/infra2salt

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/infra2salt.svg
    :alt: Supported versions
    :target: https://pypi.org/project/infra2salt

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/infra2salt.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/infra2salt


.. end-badges

gather infrastructure data and render roster, pillar, etc.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install infra2salt

Documentation
=============


https://python-infra2salt.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
