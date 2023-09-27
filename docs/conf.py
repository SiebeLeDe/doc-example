# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
project = 'Mandelbrot set'
copyright = '2023, SiebeLeDe'
author = 'SiebeLeDe'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add the src directory to the path
sys.path.insert(0, os.path.abspath("../src"))

# Markdown support (myst-parser), LaTeX support (sphinx.ext.mathjax), Ability to see source code (sphinx.ext.viewcode)
extensions = ['myst_parser', 'sphinx.ext.mathjax', "sphinx.ext.autodoc", "sphinx.ext.autosectionlabel", "sphinx.ext.viewcode"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Include both .rst and .md files
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

# Removes the module name from the documentation
add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
