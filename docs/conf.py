# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------

this_path = Path(__file__).parent.resolve()
sys.path.insert(0, str(this_path / ".."))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "linkedin-posts"
copyright = "2023 Rami Boutasssghount"
author = "rami"


def _get_version() -> str:
    lines = (this_path / ".." / "pyproject.toml").read_text().splitlines()
    version_lines = [line.strip() for line in lines if line.startswith("version = ")]

    assert len(version_lines) == 1
    return version_lines[0].split(" = ")[1].replace('"', "")


version = _get_version()
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


add_module_names = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
