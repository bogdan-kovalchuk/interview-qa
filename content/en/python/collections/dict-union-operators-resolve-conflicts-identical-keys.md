---
id: py-coll-0011
title: "How do the dict union operators `|` and `|=` resolve conflicts between identical keys, and how do they differ in mutation?"
description: "How do the dict union operators `|` and `|=` resolve conflicts between identical keys, and how do they differ in mutation?"
track: python
section: collections
level: middle
type: comparison
tags: []
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L118-L138
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Both operators, on duplicate keys, keep the value from the right-hand operand; `|` returns a
new dict, while `|=` updates the left one in place.**[^py314-library-stdtypes] `d1 | d2` creates a
new dictionary; `d1` is not changed. `d1 |= d2` is equivalent to `d1.update(d2)` – it modifies
`d1` in place. The order of keys in the result: first the keys from the left operand in their own
order, then the new keys from the right.

## Detailed explanation

The `|` and `|=` operators for `dict` appeared in Python 3.9 (PEP 584) as a syntactic counterpart
to set operations – before that, merging dictionaries was done with `{**d1, **d2}` or
`dict(d1, **d2)`, both less obvious to read.[^py314-library-stdtypes]

There is an asymmetry in what each operator accepts: `d1 | d2` requires the right-hand operand to
be a `dict` (or support `keys()` like a mapping) – otherwise it raises `TypeError`. But
`d1 |= d2` is implemented through `__ior__`, which for `dict` effectively calls `update()`, so it
accepts a much wider range of types: any iterable of `(key, value)` pairs, not just a mapping.
This asymmetry mirrors the familiar pair `list.__add__` versus `list.__iadd__`, where `+=` also
accepts an arbitrary iterable while `+` accepts only the same type.

The position of a key in the result is determined only by the order of its first appearance:
`d1 | d2` is equivalent to building a copy of `d1` and then calling `update(d2)` on it, so
existing keys from `d1` keep their position in iteration order even when their value is
overwritten by a value from `d2`; new keys from `d2` are appended at the end in the order they
appear in `d2`.

Unlike `dict.update()`, which always mutates `self` and returns `None`, `d1 | d2` is an
expression that can be passed along immediately as an argument, without creating an intermediate
named variable.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
