# Pyfunctools

Pyfunctools is a module that provides functions, methods and classes that help in the creation of projects in python, bringing functional and object-oriented programming methods.

[![Documentation Status](https://readthedocs.org/projects/pyfunctools/badge/?version=latest)](https://pyfunctools.readthedocs.io/en/latest/?badge=latest)
[![Python versions](https://img.shields.io/pypi/pyversions/pyfunctools.svg)](https://pypi.python.org/pypi/pyfunctools/)
[![PyPI](https://img.shields.io/pypi/v/pyfunctools.svg)](https://pypi.python.org/pypi/pyfunctools/)
[![GitHub stars](https://img.shields.io/github/stars/natanfeitosa/pyfunctools.svg)](https://github.com/natanfeitosa/python-pyfunctools/stargazers)


## Instalation

Via PIP (recommended):
```sh
pip install pyfunctools
```

Via GitHub:
```sh
git clone https://github.com/natanfeitosa/pyfunctools.git && cd pyfunctools && pip install .
```

## Development

> Makefile commands so far only available for linux

<br>

```make init``` install development dependencies.

Run ```make auto_doc``` when adding a new submodule.

To create the documentation based on the docstrings, just run ```make gen_docs```.

Test the HTML documentation locally with the ```make server``` command.

The ```make all``` command runs the last two automatically.
