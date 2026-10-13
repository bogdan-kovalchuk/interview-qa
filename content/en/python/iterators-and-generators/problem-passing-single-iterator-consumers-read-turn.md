---
id: py-itergen-0014
title: "What problem does passing a single iterator to two consumers that read it in turn create?"
description: "What problem does passing a single iterator to two consumers that read it in turn create?"
track: python
section: iterators-and-generators
level: middle
type: practical
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
  - source_id: py314-glossary-term-iterable
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: definition of iterable; iter() returns an iterator for one pass."
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: definition of iterator and exhausted."
  - source_id: py314-library-itertools-tee
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.tee
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: itertools.tee(), independent iterators from one iterable and their storage requirements."
---

## Short answer

**An iterator is one-directional and stateful: two consumers share one cursor, so items read by one are unavailable to the other.**[^py314-library-stdtypes-iterator-types] For example, if the first consumer has taken three items, the second starts from the fourth, not the first. For both to receive the complete data, pass an iterable (for example, a `list`) from which each consumer takes its own iterator.[^py314-glossary-term-iterable] Or use `itertools.tee()`, which creates independent iterators at the cost of extra memory.[^py314-library-itertools-tee]

## Detailed explanation

An iterable is an object that can return its members one at a time. When an iterable is passed to `iter()`, the result is an iterator meant for one pass over the values.[^py314-glossary-term-iterable] An iterator returns successive items of its stream and, once no more data is available, raises `StopIteration` and becomes exhausted.[^py314-glossary-term-iterator] The iterator itself keeps the position: each `next()` takes the next item and moves forward.[^py314-library-stdtypes-iterator-types] So the position belongs to the iterator object itself, not to a consumer. If two consumers hold the same iterator, they share one position.

The example: two consumers read one iterator in turn. Each gets only part of the data, and neither sees the complete sequence. The comments show the output on CPython 3.13 and 3.14:

```python
it = iter(range(6))
a_items, b_items = [], []
for _ in range(3):
    a_items.append(next(it))        # consumer A reads one item
    b_items.append(next(it))        # consumer B reads the next one
print('A:', a_items, 'B:', b_items) # A: [0, 2, 4] B: [1, 3, 5]
```

The first fix is to pass an iterable instead of an iterator. A container should return a new iterator on each `iter()` call, so each consumer gets its own position, starting from the beginning.[^py314-reference-datamodel-object-iter] For example, `list(values)` can be called twice on the same list, and each call starts from the first element. If the source is itself an iterator, such as a generator, it can only be stored in a `list` or split with `tee()`.

The second fix is `itertools.tee()`, which returns several independent iterators over one source:[^py314-library-itertools-tee]

```python
import itertools

it = iter(range(4))
x, y = itertools.tee(it, 2)
print(list(x), list(y))             # [0, 1, 2, 3] [0, 1, 2, 3]
```

`tee()` has a cost. The documentation warns that it may require significant auxiliary storage. If one iterator uses most or all of the data before another one starts, `list()` is faster.[^py314-library-itertools-tee]

The problem arises only when consumers hold the same iterator. A generator passed to two consumers has the same problem, because a generator is an iterator itself. If each consumer calls `iter()` on the iterable itself, there is no shared position.[^py314-reference-datamodel-object-iter]

**Common mistakes:**
- passing one iterator or generator to two functions and expecting each to receive the full sequence;
- treating `tee()` as free: it may require significant extra storage;
- converting an iterator to a `list` without checking the size of the data: if the data does not fit in memory, that is a separate problem.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
