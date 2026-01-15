# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate JCPenney Credit Card'
copyright = '2025, JCPenney'
author = 'JCPenney Support Team'

release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_title = "How to Activate Your JCPenney Credit Card"
html_short_title = "JCPenney Card Activation"
html_favicon = 'favicon.ico'

html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

html_theme_options = {
    'show_powered_by': False,
}

# html_static_path = ['_static']
