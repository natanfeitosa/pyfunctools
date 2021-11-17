init: ; pip install -r requirements.txt

auto_doc: ; sphinx-apidoc -MT -feo docs pyfunctools

gen_docs: ; cd docs ; make html ; cd ..

server: ; python -m http.server 3000 --directory ./docs/_build/html

all: ; make gen_docs ; make server
