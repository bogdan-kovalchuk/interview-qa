---
id: py-coll-0022
title: "Why does membership in a list usually cost linear time, while a set or dict is expected to give average constant-time lookup?"
description: "Why does membership in a list usually cost linear time, while a set or dict is expected to give average constant-time lookup?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L540-L592
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**For a `list`, the `in` operator does a linear search: it compares `x` against every element via
`==` – O(n).**[^py314-library-stdtypes] `set` and `dict` in CPython use a hash table: `hash(key)`
is computed, the bucket is located from it, and `==` is only called there – average O(1).
<span class="warn">In the worst case (many collisions), hash table lookup degrades to
O(n).</span>

## Detailed explanation

A `list` has no auxiliary structure tying a value to a position: the only way to check
`x in lst` is to walk the elements one by one and compare each with `==`, until a match is found
or the list runs out. This is linear by definition, regardless of whether the list is sorted or
not; there is no way to do better than O(n) without building an extra structure, because a `list`
has no index by value, only an index by position.[^py314-library-stdtypes]

`set` and `dict` instead index elements by `hash(x)`: a value lands in a specific bucket right at
insertion time, so a lookup computes `hash(x)` once and checks only the candidates in that bucket
– on average one or two elements, not all n. CPython keeps this "on average" true by automatically
growing the table once it is more than roughly two-thirds full, so the load factor, and with it
the length of the probe sequence, stays small even as the number of elements grows.

This advantage costs two things. First, `set`/`dict` elements must be hashable – a list or other
mutable container cannot be put into a `set` at all, so for collections of lists you either
convert them to `tuple` or stay with linear search over a `list`. Second, building the `set` from
an existing `list` in the first place costs O(n) plus extra memory for the hash table – worth it
when membership is checked repeatedly (`m` checks against a `set` cost O(n + m) in total, versus
O(n * m) for a `list`), but not worth it for a single check on a small collection, where the
overhead of building and hashing can outweigh the gain.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
