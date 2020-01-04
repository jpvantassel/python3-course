# Python Modules

> Joseph P. Vantassel, The University of Texas

## One-Minute Summary

- A Python module is a text file with a `.py` file extension that contains
Python code.
- Modules are used primarily to organize code (typically functions or
classes) related to a particular use case.
- Modules can be loaded using the keyword `import`.
- Import statements generally appear in the firt few lines of a Python program
with syntax similar to the following:

```python3
import this             # GOOD - Import contents in namespace this.
from this import that   # OK - Import one specific content (that) from this.
from this import *      # BAD - Import all contents without maintaining the namespace.
```

## Why Modules

Python modules allow code written in one file to be imported into another. The
ability to import code into one main file allows it to be kept clean of
excess function and class definitions, thereby allowing the user to focus on
_what_ the program is doing rather than _how_ it is being done. Additionally,
since the code has already been broken into multiple files with each file
containing code pertaining to a particular purpose, modules encourage and
simplify code reuse.

## Basic Usage

To see the benefits of modules, we need to first have a snipped of code that we
think we may want to reuse in the future. For this example we will use root
search algorithms, specifically a simple bisection routine. Since our file will
contain root search algorithms we name our moduel `rootsearch.py`. Its contents
are show below.

> rootsearch.py

```python3
def bisection(func, positive_guess, negative_guess, ntrials=50, tolerance=1E-6):
    """Finds the root of a function `func` using the method of bisection."""
    y_upper = func(positive_guess)
    assert(y_upper > 0)
    y_lower = func(negative_guess)
    assert(y_lower < 0)
    for _ in range(ntrials):
        new_guess = (positive_guess + negative_guess)/2
        y_new = func(new_guess)
        if abs(y_new) < tolerance:
            return new_guess
        if y_new < 0:
            negative_guess = new_guess
        else:
            positive_guess = new_guess
    return RuntimeError("Maximum number of iterations exceeded. Consider increasing ntrials or decreasing tolerance.")
```

With our re-usable bisection function defined, let's test it out. To do this we
will import our rootsearch module and use our bisection function to find the
root of a linear and parabolic equation.

> tester.py

```python3
import rootsearch as rs

# Line
def line(x, m=3, b=2):
    return (m*x + b)

line_root = rs.bisection(func=line, positive_guess=100, negative_guess=-100)
print(f"The root of y=3x+2 is x={line_root}")                        # x=-0.6666

# Parabola
def parabola(x, a=2, b=4, c=-1):
    return (a*x**2 + b*x + -50)

parabola_root = rs.bisection(func=parabola, positive_guess=10, negative_guess=0)
print(f"One of the roots of y=2x**2+4x-1 is x={parabola_root}")      # x=+4.0990
```

Rather than using the syntax `import rootsearch as rs` we could also have used
`from rootsearch import bisection` so wherever we had `rs.bisection`
we could instead use `bisection` (see alternate code below). While this second
method appears cleaner and easier to understand it should be avoided because it
abandons the protection and additional context the namespace provides.

> tester.py (alternate form)

```python3
from rootsearch import bisection

# Line
def line(x, m=3, b=2):
    return (m*x + b)

line_root = bisection(func=line, positive_guess=100, negative_guess=-100)
print(f"The root of y=3x+2 is x={line_root}")                   # x=-0.6666

# Parabola
def parabola(x, a=2, b=4, c=-1):
    return (a*x**2 + b*x + -50)

parabola_root = bisection(func=parabola, positive_guess=10, negative_guess=0)
print(f"One of the roots of y=2x**2+4x-1 is x={parabola_root}") # x=+4.0990
```

### A Warning

A pervasive practice when importing modules is to use the syntax
`from module import *`, this imports everything from `module` without
preserving the namespace. This __should almost always be avoided__ as you may
accidentally use variable, function, or classe names that are the same as those
inside `module` and unwittingly overwrite them. By doing so the module may no
longer appear to work leading you to beleive the bug is in the module and not
the code you have written. Namespaces after all _"are one honking great idea"_
and we should embrace their use.

## Sources

[Zen of Python](https://www.python.org/dev/peps/pep-0020/)
