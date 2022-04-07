# `subprocess`

> Joseph Vantassel, The University of Texas at Austin

[![License](https://img.shields.io/badge/license-CC--By--SA--4.0-brightgreen.svg)](https://github.com/jpvantassel/python3-course/blob/main/LICENSE.md)

_Note: this module assumes the user is on a *nix type machine if you are using
Windows machine you will need to modify the examples below for compatibility._

## One-Minute Summary

- `subprocess` is a module from the Python standard library for launching and handling new processes.
- `subprocess.run()` is the recommended way of using the `subprocess` module for most use cases.

- Basic syntax:

```python3
import subprocess
subprocess.run("ls")                         # List current directory *nix
# subprocess.run("cd")                       # List current directory Windows
```

## What is `subprocess`

`subprocess` is a module from the Python standard library for handling processes.
`subprocess` allows access to the machine's command line interface
(e.g., `cmd` on Windows or `shell` on *nix) directly through Python. This can be
extremely useful for automating tasks involving other programs which are callable
from the command line. Some example use cases include: launching a large number of
analyses in serial, checking the scalability of a program using different
numbers of threads and/or processors, and stitching together various independent
executable programs into a single automated workflow using Python.

## Getting Started with `subprocess`

1. [Install a modern Python interpreter](../intro/installing_python.md) if you have not
done so previously.

2. Create a new module called `launcher.py`. If you do no know what a Python
module is, [see this explainer](../intro/modules.md).

3. Start the tutorial below.

## `subprocess` Tutorial

### A simple example

Below is a very simple `subprocess` program, which will print the contents
of your current working directory.

```python3
import subprocess
subprocess.run("ls")                         # List current directory *nix
# subprocess.run("cd")                       # List current directory Windows
```

To perform a different command line operation or to launch a separate program
replace the text above with the desired syntax. For example is I have an
executable called `a.out` and I want to launch it using Python, you would simple
swap `"ls -la"` above with `"a.out"`.

### Proving additional arguments

There are two ways of proving additional arguments using subprocess the first is
by proving them as a single string and the second is by proving them as a sequence (preferred).
Both are illustrated below:

```python3
import subprocess
subprocess.run("ls -la", shell=True)         # Generally requires shell=True.
subprocess.run(["ls", "-la"])                # Does not require shell=True.
# subprocess.run("cd")                       # List current directory Windows.
```

_Note using `shell=True` has important security implications, please review
and understand these implications. Further information is provided
[here](https://docs.python.org/3/library/subprocess.html#security-considerations)._

### Capturing the output

Once we are able to launch our program using Python we may want to be able to
capture the result and parse it for future use in our Python program. For example:

```python3
import subprocess
cproc = subprocess.run(["ls", "-la"], capture_output=True, encoding="utf8") # Capture output as utf8.
print(cproc.stdout)                                                         # Print the stdout from the completed process.
print(cproc.returncode)                                                     # Can also view the return code.
```

### Reading inputs and/or writing outputs to file

Reading inputs and writing outputs is easy with `subprocess` an example of writing
`stdin` to file is shown below.

```python3
import subprocess
with open("stdout.tmp", "w") as f:           # Create file object f.
  subprocess.run(["ls", "-la"], stdout=f)    # Write stdout to f.
```

_Note: this example could easily have been performed to illustrate standard
input  (`stdin`) or standard error (`stderr`)._

### Ensuring the process completed successfully

As you may have realized by now, `subprocess.run()` will run successfully regardless
of whether the program being called ran successfully. This may not always be desirable.
To ensure the subprocess was successful you can either check the return code manually
or use the `check=True` option (recommended). For example:

```python3
import subprocess
subprocess.run(["ls", "-la"], check=True)    # Will raise CalledSubprocessError if non-zero exit code.
```

## Sources

[subprocess Documentation](https://docs.python.org/3/library/subprocess.html)
