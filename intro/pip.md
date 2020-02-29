# Pip (Pip Installs Packages)

>Joseph Vantassel, The University of Texas at Austin

[![License](https://img.shields.io/badge/license-CC--By--SA--4.0-brightgreen.svg)](https://github.com/jpvantassel/python3-course/blob/master/LICENSE.md)

## One-Minute Summary

- `pip` is a command line tool for installing Python packages.
- Basic syntax:

```bash
pip -h                           # Print help.
pip install <package>            # Install package (e.g., pip install numpy).
pip uninstall <package>          # Remove unwanted package.
pip list                         # View all currently installed packages.
```

- Complex syntax:

```bash
pip install -e <path-to-setup.py>              # An "editable" install.
pip install <*.tar.gz>                         # Install from source distribution.
pip install <*.whl>                            # Install from build distribution.
pip install git+ssh://git@rmturl/usrnm/pkg.git # Install directly from github.
```

## What is pip

Pip is a command-line tool for managing Python packages. Packages are groupings
of Python (and in certain cases other languages such as C or C++) codes to
perform a particular task. Popular packages in science and engineering include:
`numpy`, `scipy`, `pandas`, and `matplotlib`.

## How Does it Work

When you use `pip` to install a package, it queries the
[Python Package Index](https://pypi.org/) (PyPI) for the package name. If it
finds a matching package it downloads, installs, and appends it to your list of
available Python packages. If `pip` cannot find a matching package it will
return a message stating that a package by that name could not be found.

## Getting Started with pip

1. [Install a modern Python interpreter](./installing_python.md) if you have not
done so previously.

2. Open a terminal, either Windows Powershell (recommended) or Command Prompt on
a Windows machine.

3. Use the terminal to follow the tutorial below.

## Pip Tutorial

### Installing a Package

Get started with `pip` by installing a new package. We will use `numpy` as an
example.

```bash
pip list                 # View the currently installed packages.
pip install numpy        # Install numpy.
pip list                 # Note the addition of numpy and its version.
```

_Note: If you already had `numpy` installed, this example was probably not that
illustrative as you likely received a message stating with
`Requirement already satisfied: ...`. So to better understand the process try
the above procedure for a different package that you have not yet installed.
Some useful packages include: `scipy`, `pandas`, and `matplotlib`._

### Uninstall a Package

The syntax for uninstalling a package is nearly identical to installing one. We
will again use `numpy` as an example.

```bash
pip list                 # Note numpy.
pip uninstall numpy      # Uninstall numpy. Confirm file removal if required.
pip list                 # Note numpy has been removed from the list.
```

If you would like to keep `numpy` installed for future use, simply repeat the
[installation process](#Installing-a-Package).

### Installing a Python Package from Non-Traditional Sources

`pip` is generally used to install from PyPI, however this may not always be
the case.

#### Creating an Editable Install

If you are developing a Python package for either private use or public
distribution on PyPI, it is extremely useful to have a dynamically updated
version of your package accessible on your machine. The syntax for a dynamic
installation (more commonly referred to as an editable install) is simple.

```bash
pip uninstall <mypkg>             # Uninstall previous version if it exists.
pip install -e <path-to-setup.py> # Install an editable version.
```

After performing the editable installation, anytime you edit the source of your
package, the edits will be instantly made available. This removes the need to
uninstall and reinstall your package to perform testing or begin production.

#### Installing from a source distribution

If a package is private or simply not yet ready to be released on PyPI the
author may release a non-platform specific source distribution (essentially a
compressed tarball of all the necessary files to install the package).
Fortunately `pip` makes handling source distributions simple.

```bash
pip list                        # View currently installed packages.
pip install <*.tar.gz>          # Install from source distribution.
pip list                        # See the new package installed from source.
```

#### Installing from a built distribution

A built distribution may be used in similar cases as a source distribution,
however built distributions are platform specific, though they, in return,
enlist shorter installation times. Regardless the `pip` syntax is similar in
both cases.

```bash
pip list                        # View currently installed packages.
pip install <*.whl>             # Install from build distribution.
pip list                        # View the new package installed from built wheel.
```

#### Installing from Github Repository

For small open-source projects the author may not want to go through the trouble
of submitting their project to PyPI and so may only provide their code on GitHub
_Note: Other version control systems (VCS) are supported however are not
discussed here, see the `pip` documentation for details._

The exact syntax for the GitHub path can be tricky to get correct, but it will
follow the format described below if using `ssh`.

```bash
pip list                        # View currently installed packages.
pip install git+ssh://git@rmturl/usrnm/pkg.git # Install directly from GitHub.
pip list                        # View the new package installed from GitHub.
```

Note this method of installation will not work with any GitHub repository with
Python code. First, the GitHub repository must be public or you must have been
granted access. Second, the author(s) of the repository must have setup the
code to be "package ready" (i.e., it contains at a minimum a `setup.py` with the
necessary installation instructions for `pip`). If it is not clear from the
provided documentation if a package is `pip` install ready, ask the author and
express your interest in the package, but understand that it being `pip` install
ready is rather unlikely.

## Sources

[Pip Documentation](https://pip.pypa.io/en/stable/reference)

[Pip and git](https://pip.pypa.io/en/stable/reference/pip_install/#git)

[Stack Overflow: git-clone works pip install does not](https://stackoverflow.com/questions/48689415/git-clone-works-but-not-pip-install-for-the-same-remote-url)
