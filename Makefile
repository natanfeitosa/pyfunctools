init: ; pip install -r requirements.txt

autodoc: ; sphinx-apidoc -MT -feo docs pyfunctools

gendocs: ; cd docs ; make html ; cd ..

server: ; python -m http.server 3000 --directory ./docs/_build/html

all: ; make gendocs ; make server
