# Developing a Python Package
>Joseph Vantassel, The Univeristy of Texas at Austin

### Development Installs
When you are developing a python package you may want to be able to test out your package, in your real workflow, before you are ready to release your first stable version. To facilitate this, Python allows you to do what is called a development install. You will have direct access to the library as if it were installed regularly using `pip`, but the files can remain in a directory that is not your packages directory for ease of editing. You can do this in several ways.<br>

__Development Install__
```Python
python setup.py develop        # Use development install
pip install -e .               # Use pip to da an equivalent development install
pip install --user -e .        # Use pip to install for a single user
```

__Development Uninstall__
```Python
python setup.py develop --uninstall # Uninstall the development install
pip uninstall -e .                  # Use pip to do the Uninstall
pip uninstall --user -e .           # Use pip to do the uninstall for a single user
```
