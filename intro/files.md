# Reading and Writing from a File

> Joseph P. Vantassel, The University of Texas at Austin

[![License](https://img.shields.io/badge/license-CC--By--SA--4.0-brightgreen.svg)](https://github.com/jpvantassel/python3-course/blob/master/LICENSE.md)

## One-Minute Summary

- Basic Syntax:

```python3
# Write to utf-8 encoded text file
with open("example.txt", "w", encoding="utf8") as f:
  f.write("Example text")
```

```python3
# Read from utf-8 encoded text file
with open("example.txt", "r", encoding="utf8") as f:
  text = f.read()
print(text)
```

- Advanced Syntax:

```python3
# Write to json
import json
data = {"str":"value",
        "list":[0,1,2,3],
        "dict":{"subkey":"subvalue"},
        "bool":True}
with open("example.json", "w") as f:
  json.dump(data, f)
```

```python3
# Read from json
import json
with open("example.json", "r") as f:
  data = json.load(f)
print(data)
```

```python3
# Write HDF5
import numpy as np
import h5py
array = np.linspace(0, 1, 100000)
with h5py.File("example.hdf5", "w") as f:
  dset = f.create_dataset("ex", data=array)
```

```python3
# Read HDF5
import numpy as np
import h5py
with h5py.File("example.hdf5", "r") as f:
  array = f["ex"][:]
print(array.shape)
```

## Text Files

Working with files in Python requires three steps to be performed:

1. Open the file (i.e., acquire the resource).
2. Read/Write from/to the file.
3. Close the file (i.e., free the resource).

### Writing to a Text File

#### The Old Way

Below is a simple example where we use the "old" way of writing to a file.

_Note this method is only being shown for illustrative purposes the "new" way
(using context managers) is shown next._

```python3
f = open("example.txt", "w")    # 1. Open the file and acquire the resource
f.write("Hello World!")         # 2. Write text to the file
f.close()                       # 3. Close the file and free the resource
```

This example clearly shows the three steps involved in writing to a file, and
should be familiar to those who have done this process in other languages.
However, Python offers us a better and more general way of performing
these three steps using what is called a context manager. While a full
discussion of context managers is beyond the scope of this module, context
managers provide an abstraction for handling a resource (in this case a text
file). Context managers exist for making your Python program's cleaner by
removing boiler-plate syntax.

##### The New Way

The "new" way (i.e., using a context manager).

```python3
with open("example.txt", "w") as f:   # Open file for writing and save as f
  f.write("Hello World!")             # Write to file
                                      # End of indent frees the resource
```

Using a context manager allowed us to reduce the lines of code from
three to two, and abstracts away the resource handling details.

### Reading from a File

To read that information back into Python.

```python3
with open("example.txt", "r") as f:   # 1. Open file for reading and save as f
  data = f.read()                     # 2. Read data from file in string
                                      # 3. End of indent frees the resource
print(data)                           # Print out file info
```

Once you have read the contents of your file its easy to split it apart by
delimiters or end-of-line characters using the build-in methods of string
objects. Some useful methods include `split()` and `splitlines()` which will
split the string based on an entered argument and end-of-line characters,
respectively.

## Other File Types

This section includes information for working with other commonly-used file
types.

### JSON

JaveScript Object Notation (JSON) is a light-weight data interchange format
designed to be easy for both humans and machines to read and write. As its name
implies, JSON was created as for the JavaScript language,
however has since been integrated in nearly all major programming languages.

JSON is best for small amounts of data (a few hundred lines) where the data
has some complex underlying structure that needs to be preserved. JSON is not
recommended when dealing with large amounts of data or if another simpler data
format is available. For example prefer storing a series of 1D arrays as columns
in a csv file rather than as a group of objects in JSON. If you have a large
amount of data see the HDF5 section below.

Reading and writing JSON requires the `json` module which is included as
part of the Python Standard Library (i.e., no `pip install` required).

In this first example we wish to write a dictionary called `data` which includes
four keys: `str`, `list`, `dict`, and `bool`. Each of these keys are associated
with data. We use the `dump` command from the `json` module to dump the
dictionary to the file `example.json`.

```python3
import json
data = {"str":"value",
        "list":[0,1,2,3],
        "dict":{"subkey":"subvalue"},
        "bool":True}
with open("example.json", "w") as f:    # Context manager opens file as f
  json.dump(data, f)                    # Dump dictionary to file
                                        # End indent frees the resource
```

Viewing `example.json` we see the JSON syntax is similar to the syntax of the
Python dictionary we started with.

```json
{"str": "value", "list": [0, 1, 2, 3], "dict": {"subkey": "subvalue"}, "bool": true}
```

To read the data back into Python.

```python3
import json
with open("example.json", "r") as f:    # Context manager opens file as f
  data = json.load(f)                   # Load data into variable data
print(data)                             # Print data
```

### HDF5

HDF5 is a binary data format designed for handling large datasets. We will use
the `h5py` package, however `h5py` is not the only Python package to facilitate
reading and writing HDF5 files. `h5py` is not part of the standard library and
therefore requires a `pip` install (i.e., `pip install h5py`). `h5py` works
closely with `numpy` so you will want to install that as well before following
the examples below (i.e., `pip install numpy`).

Let's write a `list` of `int` to an HDF5 file.

```python3
import numpy as np
import h5py
mydata = [1,2,3,4,5]                             # List of 5 integer values
with h5py.File("list_example.hdf5", "w") as f:   # Open hdf5 file as f
  dset = f.create_dataset("mylist", data=mydata) # Name as "my_list"
```

Let's read that data back into Python.

```python3
import numpy as np
import h5py
with h5py.File("list_example.hdf5", "r") as f:   # Open hdf5 file as f
  print(list(f.keys()))                          # View keys -> "mylist"
  data = f["mylist"][:]                          # Extract data
print(data)                                      # Print data
```

_Note that you must perform any operations with the file (`f`) and its
children (`f["mylist]`) before the end of the context manager. Otherwise,
the file will be closed and no further interactions allowed._

Now let's write a large `numpy` array to an HDF5 file.

```python3
import numpy as np
import h5py
array = np.linspace(0, 1, 100000)                # 100000 value between 0 and 1
with h5py.File("array_example.hdf5", "w") as f:  # Open hdf5 file as f
  dset = f.create_dataset("my_100k", data=array) # Save data with name "my_100k"
```

Now we read that data back in.

```python3
import numpy as np
import h5py
with h5py.File("array_example.hdf5", "r") as f:  # Open hdf5 file as f.
  print(list(f.keys()))                          # View keys -> "my_100k"
  array = f["my_100k"][:]                        # Read the data.
print(array.shape)                               # -> "(100000,)"
```

HDF5 offers much more functionality than what is shown here, however that will
be left for a future module.
