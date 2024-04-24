# Configuration file for the Sphinx documentation builder.

import os
import sys
import sphinx_rtd_theme

here = os.path.dirname(__file__)

# -- Project information

project = 'ABI Mapping Tools'
copyright = '2022, University of Auckland'
author = 'University of Auckland'

release = '0.1.0'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'nature'

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = "_images/mapclient-logo.png"
# -- Options for EPUB output
epub_show_urls = 'footnote'

# If true, enable figure numbering
numfig = True

# List of submodule packages that are using autodoc.
# Note: Assumes that the submodule uses 'src' as a package directory.
autodoc_submodules = [
    'opencmiss.argon',
    'opencmiss.exporter',
    'opencmiss.maths',
    'opencmiss.utils',
    'opencmiss.zincwidgets',
]

sys.path.append(os.path.join(here, 'mock'))

for a in autodoc_submodules:
    sys.path.append(os.path.join(here, a, 'src'))

listing = os.listdir(here)
exclude_readmes = [os.path.join(l, 'README.rst') for l in listing if os.path.isfile(os.path.join(here, l, 'README.rst'))]

# List of reStructured text files to exclude.
exclude_patterns = []
exclude_patterns.extend(exclude_readmes)

