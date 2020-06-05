# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coalapy",
    version="0.0.1",
    author="evi1haxor",
    author_email="architdwivedi.off@gmail.com",
    description="A multimodal data clustering solution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evi1haxor/CoALa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
