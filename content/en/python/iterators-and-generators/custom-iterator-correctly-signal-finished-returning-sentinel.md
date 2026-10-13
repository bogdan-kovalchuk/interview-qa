---
id: py-itergen-0003
title: "How should a custom iterator correctly signal that it is finished, and why is returning a sentinel value from `__next__` not equivalent?"
description: "How should a custom iterator correctly signal that it is finished, and why is returning a sentinel value from `__next__` not equivalent?"
track: python
section: iterators-and-generators
level: middle
type: pitfall
tags: [next]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-for
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-for-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the for statement runs its suite for each item the iterator provides and ends when the iterator is exhausted."
  - source_id: py314-library-functions-iter
    title: "Python 3.14: Library/functions"
    url: https://docs.python.org/3.14/library/functions.html#iter
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the two-argument form iter(callable, sentinel), which ends iteration when callable returns a value equal to sentinel."
  - source_id: pep-479
    title: "PEP 479: Change StopIteration handling inside generators"
    url: https://peps.python.org/pep-0479/
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "PEP 479: a StopIteration that leaves the body of a generator is replaced with RuntimeError."
---

## Short answer

**The correct way is to raise `StopIteration` from `__next__()` when no items remain.**[^py314-library-stdtypes-iterator-types] A `for` loop ends when the iterator is exhausted.[^py314-reference-compound-stmts-for] A sentinel value returned by `__next__()` does not stop the loop: the consumer receives it as the next item and keeps iterating, so without `StopIteration` the loop does not stop by itself.

## Detailed explanation

The iterator protocol defines the end through the `StopIteration` exception. A `for` loop runs its suite for each element that the iterator provides, and ends when the iterator is exhausted.[^py314-reference-compound-stmts-for] The value that `__next__()` returns is always treated by the loop as an element, so no value by itself marks the end. Once `__next__()` raises `StopIteration`, every later call must raise it again.[^py314-library-stdtypes-iterator-types]

Here is a class that returns `None` instead of raising `StopIteration`. Its `__next__()` never ends the iteration, so `islice()` is needed to stop the output:

```python
from itertools import islice

class Source:
    def __init__(self, items):
        self._items = list(items)
        self._pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._pos >= len(self._items):
            return None                  # wrong: None reaches the loop as an item
        item = self._items[self._pos]
        self._pos += 1
        return item

print(list(islice(Source([1, 2]), 5)))   # [1, 2, None, None, None]: no end on its own
```

The correct version raises `StopIteration`, and the loop ends by itself:

```python
class Source:
    def __init__(self, items):
        self._items = list(items)
        self._pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._pos >= len(self._items):
            raise StopIteration          # the end signal defined by the protocol
        item = self._items[self._pos]
        self._pos += 1
        return item

print(list(Source([1, 2])))              # [1, 2]
```

There are two limits. First, inside a generator function `StopIteration` must not be raised manually: PEP 479 replaces it with `RuntimeError`, and a generator can finish with `return` instead.[^pep-479] For example, a generator with `yield 1` followed by `raise StopIteration` gives `RuntimeError: generator raised StopIteration` when iterated.

Second, a sentinel works in the two-argument form `iter(callable, sentinel)`. There, `iter()` itself compares the value returned by `callable()` with `sentinel` and raises `StopIteration`.[^py314-library-functions-iter] The same `None` that was an ordinary element in the class above stops the loop here:

```python
values = iter([1, 2, None, 3])
for x in iter(lambda: next(values), None):
    print(x)                             # 1, then 2; the loop stops at None
```

**Common mistakes:**
- returning `None` or an empty string from `__next__()` as an end marker: the loop does not stop;
- raising `StopIteration` inside a generator function instead of using `return`: this gives `RuntimeError`;
- assuming that after the first `StopIteration` you can call `__next__()` again and get items: the exception is raised again.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
