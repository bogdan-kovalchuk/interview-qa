---
id: py-coll-0013
title: "When is a `set` better than a list for membership checks, and what element order should never be relied on as a contract?"
description: "When is a `set` better than a list for membership checks, and what element order should never be relied on as a contract?"
track: python
section: collections
level: middle
type: comparison
tags: [set]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L17-L35
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A `set` gives average-case O(1) for `in` thanks to a hash table, while a list gives O(n); so for
frequent membership checks a set is significantly faster.**[^py314-library-stdtypes]
<span class="warn">The iteration order of a set is implementation-dependent and guarantees neither
sorting nor insertion order – it must not be relied on as a contract.</span> In practice: if you
need both fast lookup and a stable order, use a dict (which preserves insertion order from Python
3.7+) or a list with a separate index.

## Detailed explanation

The speed of `in` for a `set` is explained by direct access via a hash: `hash(x)` computes a
position in the hash table, and checking presence reduces to comparing at that position (with
collision handling), whereas a `list` has no structure for direct access by value and must compare
every element in sequence.[^py314-library-stdtypes] The average O(1) case for a set holds as long
as the hash function distributes values evenly; for deliberately adversarial data or a large number
of collisions, complexity can degrade to O(n), though in practice this is rare for built-in types.

The price of that speed is a hashability requirement: elements of a `set` must implement `__hash__`
and `__eq__` consistently (equal objects must have the same hash), so a `list` or `dict` cannot be
elements of a set, while `int`, `str`, and `tuple` (with hashable contents) can. A `list` has no
such requirement and allows mutable elements and duplicates.

The iteration order of a `set` should not be confused with the iteration order of a `dict`: since
Python 3.7, `dict` is guaranteed to preserve insertion order as part of the language spec, while
`set` has never had and does not have such a guarantee – the visible sequence of elements depends
on their hash values and the history of insertions/deletions, and for strings it additionally
changes between process runs because of hash randomization
(`PYTHONHASHSEED`).[^py314-library-collections] So code that relies on a particular set traversal
order may work today and break on a different Python version or a different run – that is not a
guarantee, but an accidental side effect of the implementation.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
