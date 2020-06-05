# coalapy
[![Build Status](https://travis-ci.com/evi1haxor/coalapy.svg?token=mr4CAooD4jjgCsCvyfqv&branch=master)](https://travis-ci.com/evi1haxor/coalapy) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-383/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Say Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/architdwivedi.off%40gmail.com) [![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A `pypi` package for performing multimodal data clustering.

## Content
1. [About CoALa](#about-coala)
2. [Installation](#installation)
    - [Clone coalapy](#clone-coalapy)
    - [Install dependencies- pipenv way](#install-dependencies--pipenv-way)
    - [Install dependencies- virtualenv way](#install-dependencies--virtualenv-way)
    - [Install coalapy](#install-coalapy)
3. [Usage](#usage)
4. [Dependecy Graph](#dependency-graph)
5. [Contributions](#contributions)
6. [License](#license)

## About CoALa

**CoALa**(<ins>Co</ins>nvex-combination of <ins>A</ins>pproximate <ins>L</ins>aplacians) algorithm inside!
Know more about CoALa [here](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjVr9TXhOjpAhWQXCsKHYHNDGMQFjABegQIARAB&url=https%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fpubmed%2F31603770&usg=AOvVaw2WCVqw4fcaxMLQHn6ub7_b).

## Installation
Till it is published on `pypi`, you have to install it in editable mode from the repository clone itself. For that, follow the instructions below.

### Clone coalapy
Clone this repository and change your working directory to `coalapy/`.
```bash
$ git clone https://github.com/evi1haxor/coalapy.git
$ cd coalapy
```
Installation of dependencies can be done in two ways. Follow what you feel seem fit for you.

### Install dependencies- pipenv way
```bash
$ pip3 install pipenv
$ pipenv install
```
### Install dependencies- virtualenv way
Alternatively, if you don't want to do it `pipenv` way for whatever reason, do as following-
```bash
$ pip3 install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
If you just want to use the package-
```bash
$ pip3 install -r requirements/production.txt
```
If you want to tinker around with the build of this repository-
```bash
$ pip3 install -r requirements/dev.txt
```
### Install coalapy  
This step is only for those who have followed above steps with `virtualenv`-
```bash
$ pip3 install -e .
```

## Usage
You can refer `main.py` file as a sample script regarding the usage. 

## Dependency Graph
```bash
black==19.10b0
  - appdirs [required: Any, installed: 1.4.4]
  - attrs [required: >=18.1.0, installed: 19.3.0]
  - click [required: >=6.5, installed: 7.1.2]
  - pathspec [required: >=0.6,<1, installed: 0.8.0]
  - regex [required: Any, installed: 2020.5.14]
  - toml [required: >=0.9.4, installed: 0.10.1]
  - typed-ast [required: >=1.4.0, installed: 1.4.1]
pandas==1.0.4
  - numpy [required: >=1.13.3, installed: ?]
  - python-dateutil [required: >=2.6.1, installed: 2.8.1]
    - six [required: >=1.5, installed: 1.15.0]
  - pytz [required: >=2017.2, installed: 2020.1]
pytest==5.4.3
  - attrs [required: >=17.4.0, installed: 19.3.0]
  - more-itertools [required: >=4.0.0, installed: 8.3.0]
  - packaging [required: Any, installed: 20.4]
    - pyparsing [required: >=2.0.2, installed: 2.4.7]
    - six [required: Any, installed: 1.15.0]
  - pluggy [required: >=0.12,<1.0, installed: 0.13.1]
  - py [required: >=1.5.0, installed: 1.8.1]
  - wcwidth [required: Any, installed: 0.2.3]
sklearn==0.0
  - scikit-learn [required: Any, installed: 0.23.1]
    - joblib [required: >=0.11, installed: 0.15.1]
    - numpy [required: >=1.13.3, installed: ?]
    - scipy [required: >=0.19.1, installed: 1.4.1]
      - numpy [required: >=1.13.3, installed: ?]
    - threadpoolctl [required: >=2.0.0, installed: 2.1.0]
```

## Contributions
Not accepting at the moment.

## License
[GPLv3](https://www.gnu.org/licenses/gpl-3.0)