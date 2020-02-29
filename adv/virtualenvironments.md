# Virtual Environments

>Joseph P. Vantassel, The University of Texas at Austin

[![License](https://img.shields.io/badge/license-CC--By--SA--4.0-brightgreen.svg)](https://github.com/jpvantassel/python3-course/blob/master/LICENSE.md)

## One-Minute Summary

- A virtual environment is an isolated Python development space with its own
Python interpreter and associated packages.
- Virtual environments allow the programmer to easily work on
multiple projects with conflicting Python interpreters and/or dependencies.
- Basic syntax

```bash
pip install virtualenv              # Install viritualenv.
virtualenv env                      # Create virtual environment named env.
source /env/Scripts/activate        # Activate the environment.
# do work ...
deactivate                          # Deactivate virtual environment.
```

- Advanced syntax

```bash
virtualenv env --python=path/to/py  # Create virtual env with specific python.
source /env/Scripts/activate        # Activate virtual environment.
pip install jupyter                 # Install Jupyter in virtual environment.
ipython kernel install --name=env   # Install Jupyter kernel in virtual environment.
jupyter notebook                    # Launch Jupyter in virtual environment.
# do work ...
deactivate                          # Deactivate virtual environment.
```

## What is a Virtual Environment

A virtual environment is an isolated space on your machine that contains a
particular Python interpreter (e.g., Python 3.7.5) and its associated packages
(e.g., numpy 1.17.0).

Virtual environment are useful because they allow multiple Python interpreters
with their associated packages to co-exist. The benefit of virtual environments
becomes obvious once you are developing or using
multiple conflicting interpreters and/or packages.

Consider for example, you are responsible for maintaining a package written
primarily in Python 3.5 with multiple out-of-date dependencies, but most of your
current projects are written in Python 3.7 with up-to-date dependencies. To
resolve this conflict you would create at least one virtual environment for one
of the
projects (e.g., Python 3.5 with the out-of-date dependencies), and develop the
other using Python 3.7 as your default interpreter. Of course you could also
create two virtual environments, one for each project. While this option
requires an additional virtual environment it is recommended because it
gives you the flexibility/agility to update interpreters and packages on
your system at will, without concern for breaking any of your previous projects.

## Getting Started

Virtual environments can be created using the `virtualenv` package. Note that a
stripped down version of `virtualenv` has been adopted into the standard
library as `venv`. However because `virtualenv` has broader functionality it
will be discussed in this module rather `venv`.

### Installing `virtualenv`

Since `virtualenv` is not part of the standard library we need to install the
package using `pip`. More information on `pip` available
[here](../1_Installing_Packages/pip.md).

```bash
pip install virtualenv                # Install the virtualenv package
```

### Creating a Virtual Environment

Now lets create a virtual environment using the host (i.e., default) Python.

```bash
virtualenv env                        # Create virtual environment called env
```

This will setup the virtual environment with the host Python interpreter and the
packages `setuptools`, `pip`, and `wheel`. These packages are for installing
other packages into the virtual environment. The installation will take a minute
or two.

### Activating the Virtual Environment

Once setup, the virtual environment needs to be activated.

#### Activating on Linux

```bash
source env/Scripts/activate           # This activates the virtual env
```

#### Activating on Windows

If you are using a Window's machine the process is slightly more complicated due
to permissions, however it can be done and clear documentation on the process
is provided [here](https://virtualenv.pypa.io/en/latest/userguide/).

### Using the Virtual Environment

Once activated, you are now in the virtual environment and can perform any
action you would do in your real environment.

```bash
pip list                              # View default installed packages.
pip install numpy                     # Install numpy into virtual environment.
pip list                              # see numpy has been added to packages
```

### Deactivating the Environment

When you are done using the environment, deactivate it. _Note this will not
delete the environment, and you can re-activate it at anytime._

```bash
deactivate                            # Deactivate virtual environment.
```

### Deleting Old Environments

To delete a virtual environment first deactivate the environment then delete the
directory with the matching name.

## Special Use Cases

### Using a Specific Version of Python

If it is not specified, `virtualenv` will use the host Python interpreter. To
use a specific Python version, first install the desired Python interpreter,
detailed instructions are provided
[here](../0_Getting_Started/installing_python.md). Second, use the following
syntax to evoke that Python interpreter in lieu of the host Python interpreter.

```bash
virtualenv env --python=path/to/py    # Use specific Python interpreter.
```

_Note:_ The path to the `python.exe` may be quite long and hard to
find, for example: `/C/Users/Joe/AppData/Local/Programs/Python/Python38/python`.
An easier way is to search for `python` at the start menu, `right-click` on
the appropriate version, and select `open file location`, then copy and path
from the top bar of file explorer.

### Using Virtualenv with Jupyter

```bash
virtualenv env                        # Create new virtual environment.
source /env/Scripts/activate          # Activate environment.
pip install jupyter                   # Install Jupyter in virtual environment.
ipython kernel install --name=env     # Install Jupyter kernel in virtual env.
jupyter kernelspec list               # List the available kernels.
jupyter notebook                      # Launch Jupyter.
```

In Jupyter, `New>env` to start a new file using the virtual environment. To use
the virtual environment with an existing file you may need to make the change
manually by selecting `Kernel>Change Kernel>env`. Regardless of how you select
the kernel, make your changes and run the notebook as usual. When done close
Jupyter and `deactivate` the virtual environment.

If you wish to remove the ipython kernel associated with the virtual environment
perform the following.

```bash
jupyter kernelspec uninstall env      # Uninstall kernel
jupyter kernelspec list               # List the available kernels.
```

## Sources

[virtualenv Documentation](https://virtualenv.pypa.io/en/latest/)

[Running Jupyter in Virtual Environment](https://medium.com/@eleroy/jupyter-notebook-in-a-virtual-environment-virtualenv-8f3c3448247)

[Stack Overflow: Removing Jupyter Kernel](https://stackoverflow.com/questions/42635310/remove-kernel-on-jupyter-notebook)
