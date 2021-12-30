# --------------------------------License Notice----------------------------------
# Python Project Boilerplate - A boilerplate project for python packages
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
# --------------------------------License Notice----------------------------------

"""Setuptools-backed setup module."""

import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="api",
    version="0.1",
    author="Guillaume Daridon",
    description="A small API example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gdarid",
    python_requires=">=3.8",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=requirements,
)
