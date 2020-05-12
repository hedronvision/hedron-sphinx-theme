"""Sphinx theme for Hedron Vision.

See: https://github.com/hedronvision/hedron-sphinx-theme
"""
from os import path


#: Full version of this project, compliant with PEP440.
__version__ = '0.0.1'


# See: https://www.sphinx-doc.org/en/master/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme('hedron_sphinx_theme', path.abspath(path.dirname(__file__)))
