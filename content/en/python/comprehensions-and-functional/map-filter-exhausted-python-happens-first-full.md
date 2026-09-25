---
id: py-compfn-0006
title: "Why can `map()` and `filter()` be exhausted in Python 3, and what happens after the first full pass over them?"
description: "Why can `map()` and `filter()` be exhausted in Python 3, and what happens after the first full pass over them?"
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: [map, filter]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**In Python 3, `map()` and `filter()` return an iterator rather than a list, so they are exhausted after the first full pass.**[^py314-howto-functional] A repeated call to `list()` on the same object yields an empty list. If the data is needed multiple times, you must either materialize it into a `list` or construct a new iterator.

## Detailed explanation

In Python 3, the built-in `map()` and `filter()` functions return lazy iterator objects of their respective types (`map` and `filter`) that compute elements on demand during iteration rather than storing them in memory.[^py314-howto-functional] They implement the standard iterator protocol via the `__iter__()` and `__next__()` methods. Each call to `next()` retrieves the next item from the underlying iterable, applies the function or predicate, and yields the result while advancing the internal cursor forward.

When the underlying iterable is exhausted or filtering completes, the iterator raises `StopIteration` and enters a terminal state. Because iterators in Python are unidirectional and by design do not cache previously yielded values, any subsequent attempt to fetch elements (such as another `list(it)` call or a new `for` loop) immediately raises `StopIteration` again. As a result, any subsequent pass yields an empty result without raising an error or warning.

This design guarantees `O(1)` memory overhead even when operating on infinite generators or massive data streams. If the transformed data is required multiple times, the developer must either explicitly materialize it into a collection (`list()`, `tuple()`) or recreate the iterator object for each pass.

Example of a `map` object becoming exhausted after the first pass:

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)

# First pass consumes all elements from the iterator
first_pass = list(squared)
print(first_pass)
# Output: [1, 4, 9, 16]

# Second pass over the same iterator finds it exhausted
second_pass = list(squared)
print(second_pass)
# Output: []
```

**Common mistakes and practical nuances:**
- passing the same `map` or `filter` object to multiple consumers (for instance, checking `if any(it): ...` partially or fully consumes the iterator before passing it to the main loop);
- expecting Python 2 semantics where `map()` and `filter()` returned a materialized `list`;
- attempting to call `len()` or access items by index `it[0]`, which raises `TypeError` because iterators do not support the sequence protocol;
- premature materialization via `list()` when handling large or infinite data streams, forfeiting the benefits of stream processing.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
