# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coalapy",
    version="0.0.1",
    author="evi1haxor",
    author_email="architdwivedi.off@gmail.com",
    description="Paper implementation- CoALa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evi1haxor/CoALa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
)
