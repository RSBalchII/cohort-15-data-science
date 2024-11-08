Here's the list of vanilla Python methods for lists, slicing, dictionaries, and tuples, formatted in markdown with descriptions in italics:

### List Methods

- `append(x)`: _Adds an item (x) to the end of the list._
- `insert(i, x)`: _Inserts an item (x) at a given position (i)._
- `remove(x)`: _Removes the first item from the list whose value is equal to x._
- `pop([i])`: _Removes the item at the given position in the list, and returns it._
- `sort(key=None, reverse=False)`: _Sorts the items of the list in place._
- `count(x)`: _Returns the number of times x appears in the list._
- `index(x[, start[, end]])`: _Returns zero-based index in the list of the first item whose value is equal to x._
- `reverse()`: _Reverses the elements of the list in place._

### Built-in Functions for Lists

- `len(s)`: _Returns the length (number of items) of an object._
- `sum(iterable, /, start=0)`: _Sums start and the items of an iterable from left to right and returns the total._
- `sorted(iterable, /, *, key=None, reverse=False)`: _Returns a new sorted list from the items in iterable._
- `list(iterable)`: _Returns a list whose items are the same and in the same order as iterable's items._
- `zip(*iterables, strict=False)`: _Iterates over several iterables in parallel, producing tuples with an item from each one._
- `enumerate(iterable, start=0)`: _Returns an enumerate object._

### Slicing

- `[:]`: _Creates a shallow copy of a list._
- `[start:stop:step]`: _Returns a new list containing elements from the original list based on the specified start, stop, and step values._

### Dictionary Methods

- `keys()`: _Returns a view object that displays a list of all the keys in the dictionary._
- `values()`: _Returns a view object that displays a list of all the values in the dictionary._
- `items()`: _Returns a view object that displays a list of the dictionary's (key, value) tuple pairs._
- `update([other])`: _Updates the dictionary with the key/value pairs from other, overwriting existing keys._
- `pop(key[, default])`: _Removes and returns the value associated with the given key if it exists in the dictionary._

### Built-in Function for Dictionaries

- `dict(**kwarg)`: _Creates a new dictionary._

### Tuple Methods

- `count(x)`: _Returns the number of times x appears in the tuple._
- `index(x[, start[, end]])`: _Returns zero-based index in the tuple of the first item whose value is equal to x._

Citations:
[1] https://docs.python.org/3/tutorial/datastructures.html
[2] https://stackoverflow.com/questions/29216889/slicing-a-dictionary
[3] https://python101.pythonlibrary.org/chapter3_lists_dicts.html
[4] https://www.geeksforgeeks.org/python-list-slicing/
[5] https://www.dataquest.io/blog/data-structures-in-python/
[6] https://numba.discourse.group/t/dynamic-heterogeneous-dictionaries-with-tuple-keys-and-non-constant-tuple-slicing/460
[7] https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/DataStructures_III_Sets_and_More.html
[8] https://www.pace.edu.in/img/course/COURSE%20MATERIAL_2ND_YEAR_18BT36_MODULE_4.pdf
[9] https://pandas.pydata.org/docs/user_guide/indexing.html
[10] https://docs.python.org/3/library/collections.html
