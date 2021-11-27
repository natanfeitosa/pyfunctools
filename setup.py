import os
from setuptools import setup

# get key package details from pyfunctools/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'pyfunctools', '__version__.py')) as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    author=about['__author__'],
    author_email=about['__author_email__'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    description=about['__description__'],
    include_package_data=True,
    keywords='package tools functional development',
    license=about['__license__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    name=about['__title__'],
    packages=['pyfunctools'],
    project_urls={
        'Documentation': 'https://pyfunctools.readthedocs.io/en/latest/install.html',
        'Source': 'https://github.com/natanfeitosa/pyfunctools/',
        'Tracker': 'https://github.com/natanfeitosa/pyfunctools/issues',
    },
    python_requires=">=3.7",
    url=about['__url__'],
    version=about['__version__'],
)
