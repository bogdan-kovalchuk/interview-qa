---
id: py-itergen-0004
title: "How do you implement a re-iterable collection so that two nested iterations do not share one cursor?"
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
---

## Short answer

**Separate the iterable from the iterator: a collection's `__iter__()` should return a new iterator on every call.**[^py314-reference-datamodel-object-iter] A typical approach is to keep the data in the collection and implement `__iter__()` as a generator function, or return a separate iterator class. Then each nested iteration gets its own independent cursor and does not interfere with the others.

```python
class MyCollection:
    def __init__(self, data):
        self._data = data
    def __iter__(self):
        for item in self._data:
            yield item
```

## Detailed explanation

Nested iterations share one cursor when the collection is itself an iterator: its `__iter__()` returns `self`, and the position is stored as an attribute of the collection. Then both loops read the same counter:

```python
class Shared:
    def __init__(self, data):
        self._data = list(data)
        self._pos = 0

    def __iter__(self):
        return self                  # the cursor lives on the collection itself

    def __next__(self):
        if self._pos >= len(self._data):
            raise StopIteration
        item = self._data[self._pos]
        self._pos += 1
        return item

pairs = Shared([1, 2, 3])
for a in pairs:
    for b in pairs:
        print(a, b)                  # only 1 2 and 1 3: the inner loop used up the shared cursor
```

The inner loop uses up the shared position, so the outer loop gets no more elements. Instead of nine pairs (3 × 3), only two come out.

The fix is to create a new iterator on every `__iter__()` call. In CPython, `iter(list)` does exactly that: each call gives a new `list_iterator` with its own position. The collection can simply delegate this work:

```python
class Collection:
    def __init__(self, data):
        self._data = list(data)

    def __iter__(self):
        return iter(self._data)      # a new list_iterator with its own position

c = Collection([1, 2, 3])
print(len([(a, b) for a in c for b in c]))  # 9: every outer item pairs with every inner item
```

A generator function, as in the Short answer, gives the same result. Each call to it returns a new generator, which is a new iterator with its own state.[^py314-reference-expressions-yield-expressions] This variant is shorter. A separate class with `__next__()` is needed when the iterator must have extra methods or explicitly managed state.

The data should be copied in `__init__()`. If you pass in a generator or another one-shot iterator and do not keep its elements, the collection is exhausted after the first pass. Calling `list(data)` stores the elements once, so every loop sees the full set.

**Common mistakes:**
- storing the position in `self` and returning `self` from `__iter__()`: nested and consecutive loops then share it;
- creating an iterator once in `__init__()` and returning it from every `__iter__()`: after the first pass, each later pass gets an exhausted iterator, which means an empty result;
- keeping the generator that was passed in, instead of its elements, and assuming the collection can be iterated many times.
