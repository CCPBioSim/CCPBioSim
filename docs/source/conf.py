# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import time

# -- Project information -----------------------------------------------------
project = "CCPBioSim"
copyright_first_year = "2026"
copyright_owners = "CCPBioSim"
author = "CCPBioSim"

current_year = str(time.localtime().tm_year)
copyright_year_string = (
    current_year
    if current_year == copyright_first_year
    else f"{copyright_first_year}-{current_year}"
)
copyright = f"{copyright_year_string}, {copyright_owners}. All rights reserved"

# -- General configuration ---------------------------------------------------
extensions = []

source_suffix = ".rst"
master_doc = "index"
language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# The shared CCPBioSim theme.
html_theme = "ccpbiosim_sphinx_theme"
html_title = "CCPBioSim Documentation"
html_context = {"github_repo": "CCPBioSim"}
html_static_path = ["_static"]
html_css_files = ["css/hub.css"]
