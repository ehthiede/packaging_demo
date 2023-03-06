# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

import os

# Project Info:

project = "wbpj"
year = "2023"
author = "Erik Henning Thiede"
version = release = "0.0.1"

copyright = "{0}, {1}".format(year, author)

extensions = [
    "sphinx.ext.mathjax",  # Equation support
    "sphinx.ext.autodoc",  # Automatically grabbing docstrings
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",  # Read Docstrings
    "sphinx.ext.viewcode",  # Links to code
]


# If we are not on readthedocs.org, we want to explicitly use their theme
# Note the theme needs to be installed, e.g. using
#
#     pip install sphinx_rtd_theme
#
on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if not on_rtd:
    html_theme = "sphinx_rtd_theme"


# Various Document Formatting Preferences
napoleon_google_docstring = True  # If using Numpy docstrings, set false
napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
