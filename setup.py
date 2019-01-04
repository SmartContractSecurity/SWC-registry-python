#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup
from setuptools.command.install import install


setup(
    name="swc-registry",
    version="0.0.7",
    url="https://github.com/SmartContractSecurity/SWC-registry-python",
    author="SmartContractSecurity",
    author_email="ersul4ik@gmail.com",
    description="The python library for accessing SWC-registry content.",
    long_description=open("README.md").read(),
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
    
)