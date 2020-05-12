"""The Sphinx theme used by Hedron Vision, available on `GitHub`_.

.. _GitHub: https://github.com/hedronvision/hedron-sphinx-theme
"""
from io import open  # Defaults to text mode with universal newlines.
from os import path

from setuptools import setup  # Prefer setuptools to distutils, always.

from hedron_sphinx_theme import __version__


# Load the README text.
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='hedron-sphinx-theme',

    # Versions comply with PEP440.
    version=__version__,

    # Short and long descriptions for PyPI.
    description='Sphinx theme for Hedron Vision',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # The project's main homepage.
    url='https://hedron-sphinx-theme.hedronvision.com',

    # Author.
    author='Hedron Vision Incorporated',
    author_email='sphinx-theme@hedronvision.com',

    # Contents of the package.
    packages=['hedron_sphinx_theme'],
    package_data={'hedron_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
    ]},
    include_package_data=True,
    zip_safe=False,

    # Tell Sphinx about our custom theme.
    entry_points={
        # See: https://www.sphinx-doc.org/en/master/theming.html#distribute-your-theme-as-a-python-package
        'sphinx.html_themes': [
            'hedron_sphinx_theme = hedron_sphinx_theme',
        ]
    },

    # Supported Python versions. Unlike the classifiers, `pip install` actually
    # checks these constraints and refuses to install projects with mismatches.
    python_requires='>=3.5, <4',

    # Project dependencies.
    # See: https://packaging.python.org/en/latest/requirements.html
    install_requires=['sphinx>=1.8'],

    # Project license.
    license='MIT License',

    # Useful keywords for search optimization.
    keywords='hedron vision sphinx theme documentation',

    # See `https://pypi.org/pypi?:action=list_classifiers`.
    # Recall that `X :: Y :: Z` is also classified as `X :: Y`.
    classifiers=[
        # How mature is this project?
        'Development Status :: 1 - Planning',

        # Under what frameworks and environments does this project operate?
        'Framework :: Sphinx :: Theme'
        'Environment :: Console',
        'Environment :: Web Environment',

        # For whom is this project intended?
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',

        # How is this project licensed? (should match `license=`)
        'License :: OSI Approved :: MIT License',

        # What Python versions are supported by this project?
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'

        # Additional classifiers.
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],

    # Additional URLs.
    project_urls= {
        'Source': 'https://github.com/hedronvision/hedron-sphinx-theme',
        'Issues': 'https://github.com/hedronvision/hedron-sphinx-theme/issues',
    },

    # TODO(sredmond): Add a cmdclass dictionary with custom commands.
)
