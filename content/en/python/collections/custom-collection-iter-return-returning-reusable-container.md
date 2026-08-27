---
id: py-coll-0018
title: "What should a custom collection's `__iter__` return, and why is returning the reusable container itself usually incorrect?"
description: "What should a custom collection's `__iter__` return, and why is returning the reusable container itself usually incorrect?"
track: python
section: collections
level: senior
type: mechanism
tags: [iter]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`__iter__` must return a new iterator (an object with `__next__`) on every call, so that
independent iterations do not conflict with each other.**[^py314-library-stdtypes] If the
container returns `self`, it becomes an iterator with one shared state: after the first
`list(obj)`, the iterator is exhausted, and a second iteration yields an empty result. The correct
implementation is `def __iter__(self): return iter(self._data)` – it creates a separate iterator
on every call.

## Detailed explanation

The iteration protocol distinguishes two different roles: an iterable (an object with `__iter__`)
and an iterator (an object with both `__iter__` and `__next__`, where the traversal state –
position, stack, index – lives in that object itself). An iterator conventionally returns `self`
from its own `__iter__` – that is fine, because an iterator is single-use by definition. The
problem arises when a container meant to be reused plays the role of the iterator itself: then
all the traversal state, such as the current index, lives in the container object itself rather
than in a separate entity.[^py314-library-stdtypes]

The most visible symptom is nested loops over the same object: `for x in obj: for y in obj: ...`
breaks the outer loop, because the inner loop advances the same shared position pointer, and
after the inner loop exits, `obj` is already exhausted for the outer one.

The simplest way to guarantee a new iterator on every call is to write `__iter__` as a generator
function: `def __iter__(self): yield from self._data`. Calling a generator function always
creates a new generator object with its own execution frame, even when the same function is
called many times in a row on the same `self`, so no state conflict occurs.

Delegating via `iter(self._data)` works similarly – it creates a fresh iterator over the
underlying data structure each time, rather than reusing one and the same object. This is
critical for structures that support parallel, independent traversals, such as a tree with
several simultaneous DFS passes.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
