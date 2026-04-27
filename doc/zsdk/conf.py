# Copyright 2026 NXP
# SPDX-License-Identifier: BSD-3-Clause
#
# ZSDK documentation build configuration.

import json
import os
import sys
from pathlib import Path

ZSDK_BASE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ZSDK_BASE / "doc" / "scripts" / "_utils"))
import utils

ZEPHYR_BASE = utils.get_projdir("zephyr")
sys.path.insert(0, str(ZEPHYR_BASE / "doc" / "_extensions"))

# -- Project information -------------------------------------------------------

project = "NXP Zephyr Project"
copyright = "NXP, 2026"
author = "NXP"
language = "en"

is_release = tags.has("release")  # pylint: disable=undefined-variable

with open(ZSDK_BASE / "doc" / "versions.json", "r", encoding="utf-8") as f:
    versions_data = json.load(f)

version = versions_data[0]
release = version

# -- Extensions ----------------------------------------------------------------

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.graphviz",
    "sphinx.ext.imgmath",
    "sphinx.ext.extlinks",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "zephyr.external_content",
    "zephyr.doxyrunner",
    "myst_parser",
    "zephyr.gh_utils",
    "mcux_book_theme.extensions.toc_builder",
]

# -- General configuration -----------------------------------------------------

master_doc = "index"
templates_path = []
todo_include_todos = True

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
    ".txt": "markdown",
}

suppress_warnings = [
    "myst.xref_missing",
]

# -- External content ----------------------------------------------------------

external_content_contents = [
    (ZSDK_BASE / "doc", "*.md"),
    (ZSDK_BASE / "doc", "*.rst"),
    (ZSDK_BASE / "doc", "pictures/*"),
    (ZSDK_BASE / "doc", "releases/*"),
    (ZSDK_BASE / "doc", "wireless/*"),
]

# -- Cross-docset TOC builder --------------------------------------------------

toc_builder_docsets = [
    {
        "docset": "zsdk",
        "title": "NXP Zephyr Project",
        "doc_root": str(ZSDK_BASE / "doc"),
        "index_file": str(ZSDK_BASE / "doc" / "index.rst"),
    },
    {
        "docset": "zephyr",
        "title": "Zephyr Project",
        "doc_root": str(ZEPHYR_BASE / "doc"),
        "index_file": str(ZEPHYR_BASE / "doc" / "index.rst"),
        "content_root": str(ZEPHYR_BASE),
    },
]

# -- HTML output ---------------------------------------------------------------

html_theme = "mcux_book_theme"
html_title = "NXP Zephyr Project"
html_show_sphinx = False
html_last_updated_fmt = "%b %d, %Y"

html_theme_options = {
    "repository_url": "https://github.com/nxp-zephyr/nxp-zsdk",
    "show_toc_level": 2,
    "collapse_navigation": True,
    "navigation_with_keys": True,
    "show_navbar_depth": 1,
    "navigation_depth": 3,
    "use_sidenotes": True,
    "home_page_in_toc": True,
    "enable_cross_docset_nav": True,
}

html_static_path = [str(ZSDK_BASE / "doc" / "_static")]
html_css_files = ["custom.css"]

version_url_template = os.environ.get(
    "DOCS_VERSION_URL_TEMPLATE", "zsdk/{version}/html/zsdk"
)
version_list = [
    (v, version_url_template.format(version=v)) for v in versions_data
]

docgen_branch = os.getenv("DOCGEN_BRANCH")
docgen_rev = os.getenv("DOCGEN_REV")

html_context = {
    "show_license": True,
    "docs_title": "NXP Zephyr Project",
    "is_release": is_release,
    "repository_url": html_theme_options.get("repository_url"),
    "current_docset": "zsdk",
    "docsets": utils.ALL_DOCSETS,
    "current_version": versions_data[0],
    "versions": tuple(version_list),
    "branch_info": docgen_branch,
    "rev_info": docgen_rev,
}

# -- Intersphinx ---------------------------------------------------------------

intersphinx_mapping = dict()

zephyr_mapping = utils.get_intersphinx_mapping("zephyr")
if zephyr_mapping:
    intersphinx_mapping["zephyr"] = zephyr_mapping

# -- Sphinx Copybutton ---------------------------------------------------------

copybutton_prompt_text = "$ "

# -- Zephyr gh_utils -----------------------------------------------------------

gh_link_version = "main" if version.endswith("99") else f"v{version}"
gh_link_base_url = "https://github.com/nxp-zephyr/nxp-zsdk"
gh_link_prefixes = {
    "applications/.*": "",
    "samples/.*": "",
    "scripts/.*": "",
    "tests/.*": "",
}


# -- Setup ---------------------------------------------------------------------

def setup(app):
    """Patch ReferencesResolver for Sphinx pending_xref edge cases."""
    from sphinx.transforms.post_transforms import ReferencesResolver

    original_run = ReferencesResolver.run

    def patched_run(self, **kwargs):
        try:
            original_run(self, **kwargs)
        except ValueError as e:
            if "is not in list" in str(e):
                print(f"Skipping problematic pending_xref resolution: {e}")
            else:
                raise

    ReferencesResolver.run = patched_run

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
