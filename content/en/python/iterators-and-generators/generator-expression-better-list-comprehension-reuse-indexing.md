---
id: py-itergen-0016
title: "When is a generator expression better than a list comprehension, and when does reuse or indexing make a list more appropriate?"
description: "When is a generator expression better than a list comprehension, and when does reuse or indexing make a list more appropriate?"
track: python
section: iterators-and-generators
level: middle
type: comparison
tags: []
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
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section generator expressions: the result is a generator iterator, and the expressions are evaluated lazily, when the iterator is asked for a value."
  - source_id: py314-library-stdtypes-generator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#generator-types
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Generator Types: a generator object provides the __iter__() and __next__() methods."
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section generator-iterator methods: the send(), throw() and close() methods of a generator iterator."
---

## Short answer

**A generator expression is better for a single pass over a large or infinite sequence: it computes values on request and does not store all the results.**[^py314-reference-expressions-generator-expressions] Once the generator is exhausted it yields nothing more, so it cannot be read again.[^py314-library-stdtypes-iterator-types] A list comprehension is the better choice when you need repeated reading, indexing (`lst[i]`), `len()`, slicing or to keep the results, because the list holds all the values together.

## Detailed explanation

The choice is between two models. A list comprehension runs the whole loop at once and returns a list with all the values. A generator expression returns a generator iterator, which computes the next value only when it is asked for one, through `next()` or by a `for` loop.[^py314-reference-expressions-generator-expressions] So a generator does not need memory for all the results, but it cannot answer questions that need every value at once.

The example below shows this on a short sequence: the list supports indexing and `len()`, while the generator is empty after one pass.

```python
values = [1, 2, 3]
as_list = [x * x for x in values]      # the list holds all three results
as_gen = (x * x for x in values)       # the generator computes values on demand

print(as_list[1], len(as_list))        # 4 3
print(sum(as_gen), sum(as_gen))        # 14 0: the second pass finds nothing left
# len(as_gen)                          # TypeError: object of type 'generator' has no len()
```

The memory saving of a generator is real, but it applies only to the results. The generator keeps its own state and a reference to the input iterable, so if `values` is itself a large list, that memory does not go away. In CPython, a list of a million results takes noticeably more memory than a generator over the same input; you can check this with `tracemalloc`, but the absolute numbers depend on the platform.

So a list is the better choice when the results are read several times, indexed or measured with `len()`. A generator lacks these abilities not because of memory: a generator object implements the iterator protocol (`__iter__()` and `__next__()`)[^py314-library-stdtypes-generator-types] and has no `__len__()` or `__getitem__()`; in addition, it has `send()`, `throw()` and `close()`.[^py314-reference-expressions-generator-iterator-methods] Once it is exhausted, it stays empty.[^py314-library-stdtypes-iterator-types]

**Common mistakes:**
- using a generator expression for code that reads the results twice: the second pass is empty;
- assuming that a generator is always faster than a list comprehension: it saves memory, not necessarily time;
- passing a generator where `len()` or indexing is expected, and getting a `TypeError`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
