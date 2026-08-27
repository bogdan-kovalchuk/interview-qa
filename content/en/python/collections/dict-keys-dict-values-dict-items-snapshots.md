---
id: py-coll-0017
title: "Are `dict.keys()`, `dict.values()`, and `dict.items()` snapshots, and how does their live-view nature affect later changes to the dictionary?"
description: "Are `dict.keys()`, `dict.values()`, and `dict.items()` snapshots, and how does their live-view nature affect later changes to the dictionary?"
track: python
section: collections
level: middle
type: mechanism
tags: [dict-keys, dict-values, dict-items]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L139-L153
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**No, they are live views – they reflect any change to the dictionary immediately, rather than a
snapshot taken at call time.**[^py314-library-stdtypes] Adding or removing a key in the
dictionary is immediately visible through a previously saved view object. `dict.keys()` and
`dict.items()` support set operations (union, intersection). <span class="warn">Changing the
dictionary while iterating over one of its views raises `RuntimeError`.</span> To get a snapshot
you need to explicitly make a copy: `list(d.keys())`.

## Detailed explanation

View objects are implemented as thin C structures that hold only a pointer back to the dictionary
itself, rather than copying the keys or values at the moment they are
created.[^py314-library-stdtypes] So `len(d.keys())` reads the dictionary's current size every
time, and a membership check `key in d.keys()` goes through the same hash lookup as `key in d` –
O(1), not a linear scan over a stored list.

This is a fundamental difference from Python 2, where `dict.keys()` returned a plain `list` – a
materialized copy of the keys taken at call time; for large dictionaries that wasted memory and
time building a list that was often only needed for a single pass.

`dict.keys()` and `dict.items()` support set operations (`&`, `|`, `^`, `-`) precisely because
dictionary keys are unique and hashable by definition – the same invariant that makes a set a
set. `dict.values()` does not support these operations: values can repeat and are not required to
be hashable, so treating them as a set would be incorrect.

A practical use of the set semantics is finding the difference between two state snapshots:
`added = d2.keys() - d1.keys()` gives the keys that were not there before, without building
intermediate lists or writing manual loops.

Because a view is bound to the live dictionary, iterating over it while the dictionary's size
changes falls under the same `RuntimeError: dictionary changed size during iteration` rule as
iterating over the dictionary directly.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
