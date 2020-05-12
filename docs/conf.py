"""Configure the Sphinx documentation builder for the demo documentation set.

Contained are some of the most common configuration options. For a full list,
see the documentation:

    https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
# -- Path setup --------------------------------------------------------------
# Add local extensions (or modules to document with autodoc) to sys.path here.
# Make sure to use os.path.abspath for absolute paths.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import hedron_sphinx_theme

# -- Project information -----------------------------------------------------

project = 'Sphinx theme for Hedron Vision'
copyright = '2020, Hedron Vision Incorporated'
author = 'Hedron Vision Incorporated'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'hedron_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
