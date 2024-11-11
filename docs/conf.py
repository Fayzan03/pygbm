# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Simulating Geometric Brownian Motion'
copyright = '2024, Fayzan'
author = 'Fayzan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'nbsphinx',
	'sphinx.ext.mathjax',
	'sphinx_rtd_theme',
    'sphinx.ext.githubpages',
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

import os
import sys
sys.path.insert(0, os.path.abspath('gbm_simulator/base_simulator.py'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
master_doc = 'index'

highlight_language = 'python3'

# Add the theme path
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]