# File Reading and Writing

> Joseph P. Vantassel, The University of Texas at Austin

[![License](https://img.shields.io/badge/license-CC--By--SA--4.0-brightgreen.svg)](https://github.com/jpvantassel/python3-course/blob/master/LICENSE.md)

## One-Minute Summary

Reading and writing files (and working with string-like data in general)
is quite easy with Python.

To read or write to a file has three main steps

  1. Open the file (i.e., acquire the resource).
  2. Read/Write from/to the file.
  3. Close the file (i.e., free the resource).

### Basic syntax

#### Read a file

```python3
with open("file.txt", "r", encoding="utf8") as f:
  data = f.read()
print(data)
```

#### Write to a file

```python3
with open("file.txt", "w", encoding="utf8") as f:
  f.write("Example text")
```

## Text Files

Working with text files with Python is fairly simple and contains three steps:

1. Open the file (i.e., acquire the resource).
2. Read/Write from/to the file.
3. Close the file (i.e., free the resource).

Below is a simple example where we write one line of text to a file. _Note this
is the "old" way of reading and writing files, and is being shown only for
illustrative purposes the "new" way (using context managers) is shown next._

"Old" way of writing to a text file.

```python3
f = open("example.txt", "w")    # Open the file and acquire the resource
f.write("Hello World!")         # Write text to the file
f.close()                       # Close the file and free the resource
```

This example is nice because it clearly shows the three steps involved in
writing to a file, and should be familiar to those who have done this in other
languages. However, Python offers us a better and more general way of performing
these three steps using a context manager designed for this purpose. While a
full discussion of context managers is beyond the scope of this module, they are
generally a way of abstracting away the details of handling a resource (in this
case a text file) in the off chance something goes wrong (e.g., the file is
missing, corrupted, or otherwise unavailable).

### Writing to a File

"New" way of writing to a text file.

```python3
with open("example.txt", "w") as f:   # Open file for writing and save as f
  f.write("Hello World!")             # Write to file
                                      # End of indent frees the resource
```

### Reading from a File

If we wanted to read that information back into Python we could do with

```python3
with open("example.txt", "r") as f:   # Open file for reading and save as f
  data = f.read()                     # Read data from file in string
                                      # End of indent frees the resource
print(data)                           # Print out file info
```

Once you have read the contents of your file its easy to split it apart by
delimiters or end-of-line characters using the build-in methods of string
objects. Some useful methods include `split()` and `splitlines()` which will
split the string based on an entered argument and end-of-line characters,
respectively.
