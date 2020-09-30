"""Sphinx configuration."""
from datetime import datetime


project = "asyncpixel"
author = "Leon Bowie"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
