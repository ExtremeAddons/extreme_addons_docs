# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Extreme-Addons Documentation'
copyright = '2023, Andrea Donati'
author = 'Andrea Donati'
release = '1.0'

import os
import sys

sys.path.insert(0, os.path.abspath('../../..'))

# Inseriamo il percorso al file conf.py:
sys.path.append(os.path.relpath(os.path.dirname(__file__)))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ['sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "sphinx_rtd_theme"

logo = os.path.join(os.path.relpath(os.path.dirname(__file__)), "_static", "_images", "logos",
                    "square_logo_512.png")

html_logo = logo
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'titles_only': True
}

html_theme_path = ["_themes", ]
html_static_path = ['_static']

html_favicon = "extreme_addons_32.ico"

html_css_files = [
    'css/custom.css',
]
