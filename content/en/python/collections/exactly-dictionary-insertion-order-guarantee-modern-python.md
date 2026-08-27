---
id: py-coll-0006
title: "What exactly does dictionary insertion order guarantee in modern Python, and what does that guarantee not say about the internal hash table?"
description: "What exactly does dictionary insertion order guarantee in modern Python, and what does that guarantee not say about the internal hash table?"
track: python
section: collections
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: "3.14"
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L293-L387
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Since Python 3.7, `dict` preserves elements in insertion order – this is a language guarantee,
not an implementation detail.**[^py314-library-stdtypes] The guarantee covers iteration order
(`keys()`, `values()`, `items()`), but it says nothing about the internal hash table structure.
In CPython this is implemented via a compact table with an index array and an entries array;
other Python implementations may achieve the same order a different way.

## Detailed explanation

The guarantee applies exclusively to iteration order: if you insert keys `a`, `b`, `c`, then
`keys()`, `values()`, `items()`, and `for k in d` itself will always walk them in that order. It
says nothing about where a record physically lands inside the hash table, what `hash()` value a
key has, or which bucket each one lives in – that is an implementation detail, and it can differ
between processes because of `PYTHONHASHSEED`.

In CPython (as an implementation detail since 3.6, as a language guarantee since 3.7), `dict`
physically consists of two arrays: a dense array of entries (key, value, hash), to which new
pairs are appended at the end, and a sparse index array that maps `hash(key)` to a position in
the dense array.[^py314-library-stdtypes] Iteration walks the dense array sequentially, so
insertion order is preserved automatically, while key lookup still goes through the index array
and `hash()`, meaning lookup speed does not depend on insertion order.

Two non-obvious behaviours follow from this. First, updating the value of an already-present key
(`d[k] = new_value`) does not change its position in iteration order. Second, deleting a key and
re-inserting the same key moves it to the end – that is a new position, not a restoration of the
old one, because the entry in the dense array is created anew.

Iteration order is part of the behaviour, but not part of equality semantics: `dict.__eq__`
compares only the set of key-value pairs, so `{'a': 1, 'b': 2} == {'b': 2, 'a': 1}` gives `True`
even though their iteration order differs. That is exactly why other Python implementations (PyPy,
for instance) can honour the same insertion-order language guarantee using a completely different
internal hash table structure – the behaviour is guaranteed, not a specific memory layout.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
