========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |githubactions|
        

.. |githubactions| image:: https://github.com/ehthiede/packaging_demo/actions/workflows/testing.yml/badge.svg?branch=main
    :alt: Testing Status
    :target: https://github.com/ehthiede/packaging_demo/actions

Example codebase demonstrating the components in setting up a python package.
The final package is in the main branch, different steps of the packaging procedure
are enumerated in the various branchs.

Our example code is a code that  performs weighted backprojection in one dimension.

Installation
============
To install, run 

::

    pip install -e .

in this directory.

Running the Code
================

The weighted backprojection can be imported in your python files as 

::

    import wbpj.weighted_backprojection_1d
    volume = weighted_backprojection_1d(images, angles)

If images are equispaced, then the command line interface can also be used,

::

    python -m wbpj.perform_reconstruction image_file.ny 0 172 --degrees

Running the Tests
=================
Tests can be run in your current environment using pytest,

::

    pytest tests/
