# Python Packages

> Joseph P. Vantassel, The Univeristy of Texas at Austin

## One-Minute Summary

- A Python package is a module or collection of modules inside a directory with
a moduled named `__init__.py` (note this module is typically empty).
- A Python package may contain any number of subpackages (i.e., sub-directories
with their own `__init__.py`).
- The Python Package Authority (PyPA) has created the Python Package Users Guide
(PyPUG) as the definnative reference for building and using Python packages.

## What is a Python Package

A Python package is a module or collection of modules that has/have been bundled
together for some purpose. [Modules](./modules.md) are simply saved
Python code stored in a text file with a `.py` extension. The package in a
literal sense is simply a directory containing the desired modules to be
packaged and an additional module `__init__.py` (often refered to as a dunder
init), which may be empty.

## Types of Python Packages

The main benefit of packages is that they can combine multiple modules together
and be built into what is called a distribution package. Distribution packages
are what is being installed when you use [pip](../1_Installing_Packages/pip.md).

There are two ways in which packages can be distributed either as source or
built distributions.

1. __Source Distributions__ - As-is Python code rolled into a compressed
tarball. Will install on any architecture running a complient version of Python.
2. __Built Distributions__ - Partially interpreted Python code. The old
style of built distributions were `bdist_egg` which have since been replaced by
`bdist_wheel`.

The built distribtion `bdist_wheel` can be one of the three following types

1. __Universal__ - Meaning distribution will run on Python 2 and 3.
2. __Pure Python__ - Meaning distribtuion is version specific and will run on
Python 2 or 3, but not both.
3. __Platform__ - Meaning distribution will run only work on certain operating
systems (e.g., OS X or Windows).

## Building a Package

### Requirements

To transform your collection of code into a module, you will need the following:

#### Required

- Directory with the same name as your package, inside of which is your source
code and an `__init__.py`. This directory may also contain subpackages (i.e.,
sud-directories with their own source code and `__init__.py`).
- A `setup.py`, details on this file are shown below.

#### Optional (but still important)

- A `README.md` or `README.rst` to explain what your package is all about.
- A `LICENCE` file explain how and for what your code may be used. Refer to
[this](https://choosealicense.com/) for help on selecting a license.
- A `./test` directory for all of your unittests.

#### Optional (slightly less important)

- A `./docs` directory where the documentaion for your package is stored.
- A `requirements.txt` file listing the packages required for developers (not
for users, depenencies for users are handled in `setup.py`).

### `setup.py`

After the code itself, the `setup.py` file is the mode important part of a
Python package. An example `setup.py` file is shown below with comments injected
to provide clarifications where needed.

```python3
from setuptools import setup, find_packages

setup(
  name='my_sample_project',             # Name of package, should match src directory.
  version='0.0.1',                      # major.minor.micro follow PEP440
  description='Example package',        # Short one-liner
  long_description='Long description on PyPI project page.',
  url='example.com',                    # Url for more info or link to documentation.
  author='Joseph P. Vantassel',         # Author name
  author_email='jvantassel@utexas.edu', # Author email
  liscence='GPLv3',                     # License information
  # For full listing of classifiers see (https://pypi.org/classifiers/).
  classifiers=[
    'Development Status :: 2 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GPLv3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  keywords='example practice',          # Keywords to improve search on PyPI
  packages=find_packages(exclude=['docs', 'tests*']),
  install_requires=['requests'],        # User package dependencies.
  package_data={
    'sample' : ['package_data.dat']     # Extra data codes need to run
  }
  data_files=None                       # Specify absolute path
  ]
  entry_points={
    'console_scripts':[
      'hello=example:say_hello',        # Creates cmd line wrapper for package
    ],
  }
)
```

## Distributing a Package

After having gone through the effort of packaging your Python code, you will
inevitably wnat to share it with others. You can do this in multiple ways.

### Sharing Built or Source Distribtions

Sharing a built or source distribtuion is simple and involves two steps.

- Creating the source and/or built distribtion, using the syntax
  - `python setup.py sdist` for source
  - `python setup.py bdist_wheel` for built, or
  - `python setup.py sdist bdist_wheel` for both.
- Installing from the source or built distribtion, using the syntax
  - `pip install <*.tar.gz>` if from source or
  - `pip install <*.whl>` if from built.

### Uploading to PyPI

Good documentation for this can be found on [PyPI](https://pypi.org/).

## Sources

[Packaging Init to Deploy](https://www.youtube.com/watch?v=4fzAMdLKC5k)

[PyPI Users Guide](https://pip.pypa.io/en/stable/user_guide/)

[PyPA Tutorial on Packaging](https://packaging.python.org/tutorials/packaging-projects/)

[Tutorial on setup.py](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)

[Packaging and Distributing](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project)
