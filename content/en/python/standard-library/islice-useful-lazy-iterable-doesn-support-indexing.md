---
id: py-stdlib-0005
title: "How is `islice()` useful for a lazy iterable that doesn't support indexing?"
track: python
section: standard-library
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
  - source_id: py314-library-itertools-islice
    title: "Python 3.14: Library/itertools, islice"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.islice
---

## Short answer

**`islice()` takes the first N elements, or a range of elements, from any iterable without converting it to a list.**[^py314-library-itertools-islice] It works like slice syntax for lists, but on iterators: `islice(gen, 5)` gives the first 5 elements, and `islice(gen, 2, 10, 2)` gives the elements at positions 2, 4, 6, and 8. Negative values for `start`, `stop`, and `step` are not supported.[^py314-library-itertools-islice]

## Detailed explanation

`islice()` is a slice for an iterable. Its signatures are `islice(iterable, stop)` and `islice(iterable, start, stop[, step])`. According to the documentation, it works like sequence slicing, but it does not accept negative values for `start`, `stop`, or `step`.[^py314-library-itertools-islice] It needs neither a length nor indexing: `islice` takes elements from the input iterable one at a time, so a generator, a file, or an infinite iterable is handled in the same way.

Laziness is visible with an infinite iterable: `count()` never ends, but `islice` stops at `stop`:

```python
from itertools import count, islice

print(list(islice(count(10, 5), 4)))         # [10, 15, 20, 25]: count() is infinite
print(list(islice('ABCDEFG', 2, 4)))         # ['C', 'D']
print(list(islice('ABCDEFG', 2, None)))      # ['C', 'D', 'E', 'F', 'G']
print(list(islice('ABCDEFG', 0, None, 2)))   # ['A', 'C', 'E', 'G']
```

Elements before `start` are skipped, and elements between steps of `step` are also read from the input iterable.[^py314-library-itertools-islice] For a generator this means that the skipped elements are produced. The example prints each element so that it is visible which ones are produced:

```python
from itertools import islice

def numbers():
    for i in range(6):
        print(f'produce {i}')
        yield i

gen = numbers()
print(list(islice(gen, 3)))  # produce 0, 1, 2 are printed, then [0, 1, 2]
print(next(gen))             # produce 3 is printed, then 3
print(list(islice(numbers(), 2, 6, 2)))  # produce 0 to 5 are all printed, then [2, 4]
```

In CPython, `islice` does not request an element beyond `stop`: after `islice(gen, 3)` the generator stands before the fourth element, and `next(gen)` produces it. The documentation does not describe this, so it is observed CPython behaviour rather than a language guarantee, and code should not rely on it.

**Common mistakes:**
- expecting `islice(it, -1)` to return the last element: negative values are not supported, and the call raises `ValueError`;
- assuming that `islice` leaves the input iterator alone: it advances it, and the next `next()` continues from the position where `islice` stopped;
- assuming that elements skipped by `start` or `step` are not computed: for a generator they are produced.
