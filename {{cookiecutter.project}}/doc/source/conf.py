# Configuration file for the Sphinx documentation builder.

import os
import sys

project = "{{ cookiecutter.project }}"
copyright = "{% now 'utc', '%Y' %}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"
version = "0.0.1"
release = "0.0.1"

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    "sphinxcontrib.restbuilder",
    "sphinxcontrib.globalsubs",
    "sphinx-prompt",
    "sphinx_substitution_extensions"
]

templates_path = ["_templates"]

exclude_patterns = []

html_static_path = ["_static"]

html_theme = "sphinx_rtd_theme"

master_doc = "index"

img_base_url = "https://git.beta.ucr.ac.cr/" + author + "/" + project + "/"
img_url = img_base_url + "raw/master/img/"

author_img = ".. image:: " + img_url + "author.png\n   :alt: author"
author_slogan = "Comunidad de Software Libre de la Universidad de Costa Rica."

github_base_url = "https://github.com/"
github_url = github_base_url + author + "/" + project
github_link = "`Github <" + github_url + ">`_."

gitlab_base_url = "https://git.beta.ucr.ac.cr/"
gitlab_url = gitlab_base_url + author + "/" + project
gitlab_link = "`Gitlab <" + gitlab_url + ">`_."

readthedocs_url = "https://" + project + ".readthedocs.io"
readthedocs_badge = "/projects/" + project + "/badge\n   :alt: readthedocs"
readthedocs_link = "`Readthedocs <" + readthedocs_url + ">`_."

global_substitutions = {
    "AUTHOR_IMG": author_img,
    "AUTHOR_SLOGAN": author_slogan,
    "AVATAR_IMG": ".. image:: " + img_url + "avatar.png\n   :alt: avatar",
    "FLOW_IMG": ".. image:: " + img_url + "/flow.png\n   :alt: flow",
    "GITHUB_LINK":  github_link,
    "GITLAB_LINK":  gitlab_link,
    "PROJECT": project,
    "READTHEDOCS_BADGE": ".. image:: https://rtfd.io" + readthedocs_badge,
    "READTHEDOCS_LINK": readthedocs_link
}

substitutions = [
    ("|AUTHOR|", author),
    ("|PROJECT|", project)
]
