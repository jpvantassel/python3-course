# Unit Testing

> Joseph P. Vantassel, The University of Texas at Austin

[![License](https://img.shields.io/badge/license-CC--By--SA--4.0-brightgreen.svg)](https://github.com/jpvantassel/python3-course/blob/main/LICENSE.md)

## What is Unit Testing

__Unit testing__ is the automated process of checking the result of a small
snippet of code with known inputs to ensure they produce some known output.

The snippet of code may be a function or method, but must it must at a minimum
have a clear input and known output. The known output may be the result of a
hand-calculation or a published solution from a reputable source. If using a
published solution, be sure to include a reference for posterity. In all cases
unit tests are written once (and only once) programmatically so that they can be
performed quickly and consistently.

## How to Unit Test

Various frameworks, among the most popular:

- `unittest`
- `pytest`
- `hypothesis`

In this module we will discuss the `unittest` framework.

### The `unittest` Framework

`unittest` is defined as an object oriented testing framework.

`unittest` has four main components:

1. __test fixture__ : A _test fixture_ represents the preparation and cleanup
    for testing.
2. __test case__: A _test case_ is the individual unit of testing.
3. __test suite__: A _test suite_ is a collection of test cases, test suites,
    or both. It is used to aggregate related tests and suites.
4. __test runner__: A _test runner_ is a component which orchestrates the
    execution of tests.

## Writing Unittests

The good news is that writing a unit test is easy and straightforward. And odds
are that, even if you are not currently using a unit test framework, you are
probably already "doing the hard part" by checking your code in some
adhoc manner. All you need to do is to write these adhoc tests down
programmatically so that they can be repeated quickly and precisely.

The challenging part of unit testing is selecting/developing test cases that
are significant. You may think that all of your code is significant and you
should have a test for every part of your code, and while this is a
great goal it is often impossible/impractical at a projects outset. Focus on
writing unit tests for the parts of your code
which are fragile (i.e., most easily broken during refactoring),
frequently called (e.g., methods in a base class), or have been the cause
of previous bugs. Once you have these trouble areas covered then work to get to
100% test coverage, just remember that 100% test coverage does not guarantee
that your code is correct.

### When should you write your unit tests

The best time to write a unit test is at the time you write the corresponding
code. You will already be familiar with what the code is doing and should have a
good feeling for things that could go wrong.

The second best time to write a unit test is after you have just found and fixed
a bug. You spent the time to find the bug, so use the reintroduction to your
advantage by writing a test that will prevent this bug from re-emerging in the
future.

### Where should you write your unit tests

There are two main schools of thought.

1. At the bottom of the module it is designed to test.

    __Pros__

    - Tests and code are inside a single file, which is convenient for
    non-packaged modules.
    - Do not need to change directories to run the test, by running the module
    you will automatically run its tests.

2. In a separate folder called `test` with a new file for each module.

    __Pros__

    - The test module can be run separately from the command line.
    - The test code can more easily be separated from shipped code.
    - There is less temptation to change the test, rather than fixing the code.
    - Test code should be modified less frequently than the code it tests.
    - Tests can be refactored more easily.
    - If the testing strategy changes then there is no reasons to change the
    source.

In short, if you are developing a module or package that is unlikely
to be shared, writing your tests in the same file offers some advantages,
however placing your tests in a `test` folder with one test file per module is a
more general and extensible option and is generally recommended.

### Two Simple Examples

Lets take a very simple example where we have a function called `add` which
surprisingly enough adds two numbers, and let's verify that is working
correctly.

```python
import unittest                               # Import framework

def add(a, b):                                # Standard python function
    """Add a and b and return the result."""
    return a+b

class Test_Math(unittest.TestCase):           # Define test suite. Note that
                                              # we are inheriting from TestCase

    def test_add(self):                       # Define a test case
        a = 2
        b = 2
        self.assertEqual(add(a,b), a+b)       # Call runner

if __name__ == '__main__':                    # Return result of test, if main
    unittest.main()
```

Which results in the following.

```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

And here is a more complicated example, where we want to examine some of the
built-in methods for `str` type variables.

```python
import unittest                               # Import framework

class TestStringMethods(unittest.TestCase):   # Define test suite

    def test_upper(self):                     # Define a test case
        expected = 'FOO'
        returned = 'foo'.upper()
        self.assertEqual(expected, returned)  # Call runner

    def test_isupper(self):                   # Define another test case
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):                     # And another test case
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':                    # Return result of test, if main
    unittest.main()
```

Which results in the following.

```bash
...
----------------------------------------------------------------------
Ran 3 tests in 0.007s

OK
```

## Other useful `unittest` features

### setUp() and tearDown()

Defining the methods `setUp()` and `tearDown()` in your _test suite_ allows for
repetitive preparation and clean-up operations to be defined only once for all
of the _test cases_ in the suite.

- `setUp()`: Performs any repetitive pre-test work. Runs automatically before
each _test case_.
- `tearDown()`: Performs any repetitive post-test clean-up. Run automatically
after each _test case_, regardless of whether they were successful.

```python
import unittest                               # Import framework

class TestExample(unittest.TestCase):         # Define test suite

    def setUp(self):                          # Define setUp (done first)
        print("Hello from setup()")

    def teatDown(self):                       # Define tearDown (done last)
        print("Goodbye from tearDown()")

    def test_add(self):
        expected = 5
        returned = 2 + 3
        self.assertEqual(expected, returned)  # Will pass

    def test_substract(self):
        expected = 3
        returned = 5 - 1
        self.assertEqual(expected, returned)  # Will fail

if __name__ == '__main__':                    # Return result of test, if main
    unittest.main()
```

Which results in the following.

```bash
Hello from setup()
Goodbye from tearDown()
.Hello from setup()
Goodbye from tearDown()
F
======================================================================
FAIL: test_substract (__main__.TestExample)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c/example.py", line 19, in test_substract
    self.assertEqual(expected, returned)
AssertionError: 3 != 4

----------------------------------------------------------------------
Ran 2 tests in 0.012s

FAILED (failures=1)
```

Note that `Hello from setup()` and `Goodbye from tearDown()` both appear twice,
once for each of our _test cases_ even though one of the test cases failed.

## References

[Unit Testing Framework -  Python Docs](https://docs.python.org/3/library/unittest.html)
