# Pyfunc

Pyfunc is a module that provides functions, methods and classes that help in the creation of projects in python, bringing functional and object-oriented programming methods.

[![Documentation Status](https://readthedocs.org/projects/pyfunc/badge/?version=latest)](https://pyfunc.readthedocs.io/en/latest/?badge=latest)


## Instalation

Via PIP (recommended):
```sh
pip install pyfunc
```

Via GitHub:
```sh
git clone https://github.com/natanfeitosa/pyfunc.git && cd pyfunc && pip install .
```

## Development

> Makefile commands so far only available for linux

<br>

```make init``` install development dependencies.

Run ```make auto_doc``` when adding a new submodule.

To create the documentation based on the docstrings, just run ```make gen_docs```.

Test the HTML documentation locally with the ```make server``` command.

The ```make all``` command runs the last two automatically.
