---
id: py-itergen-0001
title: "How does an iterable differ from an iterator, and what methods make up their respective protocols?"
track: python
section: iterators-and-generators
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
  - source_id: py314-reference-datamodel-object-getitem
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__
  - source_id: py314-glossary-term-iterable
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterable
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
  - source_id: py314-library-functions-iter
    title: "Python 3.14: Library/functions"
    url: https://docs.python.org/3.14/library/functions.html#iter
---

## Short answer

**An iterable is an object from which an iterator can be obtained, usually through `__iter__()`.**[^py314-glossary-term-iterable] An iterator keeps state and returns items one at a time through `__next__()`; when the items run out, it raises `StopIteration`.[^py314-glossary-term-iterator] Every iterator is also iterable, because its `__iter__()` returns the iterator itself.[^py314-glossary-term-iterator] Not every iterable is an iterator: `list`, `tuple` and `str` have `__iter__()` but no `__next__()`.

## Detailed explanation

An iterable and an iterator are two different concepts that are easy to confuse, because every iterator is also an iterable. An iterable is an object that can hand out its elements one at a time. It includes all sequences (for example `list`, `str` and `tuple`) and any class that defines `__iter__()` or a `__getitem__()` that behaves like a sequence.[^py314-glossary-term-iterable] For an iterable, the key ability is to create an iterator. The built-in `iter()` accepts an object that supports the iteration protocol (`__iter__()`) or the sequence protocol (`__getitem__()` with integer arguments starting at 0).[^py314-library-functions-iter]

An iterator is an object with state: it remembers which element it stopped at. Its protocol has two methods. `__iter__()` returns the iterator itself, which lets it be used in `for` and `in` just like a container. `__next__()` returns the next element, and when there are no more, it raises `StopIteration`.[^py314-library-stdtypes-iterator-types] The following example shows both roles on a `list`:

```python
nums = [1, 2, 3]
print(hasattr(nums, '__next__'))     # False: a list is iterable, not an iterator
it = iter(nums)                      # calls nums.__iter__() and returns a new iterator
print(type(it).__name__)             # list_iterator
print(hasattr(it, '__next__'))       # True
print(iter(it) is it)                # True: an iterator's __iter__() returns itself
print(next(it), next(it), next(it))  # 1 2 3
try:
    next(it)
except StopIteration:
    print('StopIteration')           # the iterator is exhausted
```

After `__next__()` raises `StopIteration`, every later call must raise it again.[^py314-library-stdtypes-iterator-types] An iterator does not restart. To go over the same data again, you need a new iterator, which `iter()` creates from the iterable.

Not every iterable has `__iter__()`. A class that has only `__getitem__()` also works with `iter()`, through the sequence protocol. For such a class, the iterator calls `__getitem__(0)`, `__getitem__(1)` and so on.[^py314-library-functions-iter] In CPython it stops when `__getitem__()` raises `IndexError`.[^py314-reference-datamodel-object-getitem] Having only `__iter__()` does not make an object an iterator: an iterator also needs `__next__()`, and its `__iter__()` must return the object itself.

**Common mistakes:**
- treating iterable and iterator as synonyms and calling `next()` on a list: `next([1, 2])` raises `TypeError: 'list' object is not an iterator`;
- looking for `__next__()` on a `list`, `tuple` or `str`: these are iterables, not iterators;
- assuming an iterator can be looped over twice: once exhausted, it does not start again.
