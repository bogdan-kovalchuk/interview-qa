---
id: py-coll-0010
title: "Why can changing the size of a dictionary while iterating its keys fail, while changing the value of an existing key is often allowed?"
description: "Why can changing the size of a dictionary while iterating its keys fail, while changing the value of an existing key is often allowed?"
track: python
section: collections
level: senior
type: pitfall
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L154-L172
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Iterating over a dictionary fixes its size (the number of key slots); adding or removing a key
changes that size and raises `RuntimeError: dictionary changed size during
iteration`.**[^py314-library-stdtypes] Changing the value of an existing key does not change the
table's size, so it does not break iteration. The safe pattern is to iterate over a copy of the
keys: `for k in list(d):`.

## Detailed explanation

The size check is a runtime guard inside the C-level implementation of `dict`: the dictionary
iterator remembers the number of filled slots (`ma_used`) at the time the iterator was created
and compares it against the current value on every call to `__next__`. If the counts diverge,
CPython immediately raises `RuntimeError` rather than waiting for the loop to reach a corrupted
state.[^py314-library-stdtypes] This is an implementation safeguard, not a language guarantee: the
Python specification only says that changing a dictionary's size during iteration is undefined
behaviour, and the fact that CPython catches it reliably is a detail of this particular
interpreter.

Changing the value of an existing key slips past this check, because updating a value neither
adds nor removes a slot in the table – the number of filled slots (`ma_used`) stays the same,
only the slot's contents get overwritten.

The trap is that deleting a key and then adding a different one in the same loop can also happen
to leave `ma_used` unchanged and not raise an error, but the table may have been rehashed
(resized) in between, and iteration behaviour after that is officially undefined – the absence of
an exception here does not mean the code is correct.

`dict.keys()`, `dict.values()`, and `dict.items()` are thin view wrappers over that same table
state, so their iterators fall under the same rule.

Safe alternatives besides `for k in list(d):` include building a new dictionary with a dict
comprehension (`{k: f(v) for k, v in d.items()}`) instead of mutating during traversal, or
collecting the intended changes in a separate list of operations and applying them after the loop
finishes.

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
