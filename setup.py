#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup
from setuptools.command.install import install

# circleci.py version
VERSION = "0.0.6"

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
    name="swc-registry",
    version=VERSION,
    url="https://github.com/SmartContractSecurity/SWC-registry-python",
    author="SmartContractSecurity",
    author_email="ersul4ik@gmail.com",
    description="Python library for accessing SWC-registry content.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["swc_registry"],
    include_package_data=True,
    install_requires=["requests==2.20.1"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
