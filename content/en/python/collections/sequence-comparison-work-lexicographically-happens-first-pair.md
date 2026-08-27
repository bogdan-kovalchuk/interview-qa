---
id: py-coll-0019
title: "How does sequence comparison work lexicographically, and what happens at the first pair of elements that do not support ordering?"
description: "How does sequence comparison work lexicographically, and what happens at the first pair of elements that do not support ordering?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L503-L516
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Sequences are compared lexicographically: element by element, until the first unequal pair is
found – that pair determines the result.**[^py314-library-stdtypes] If all the shared elements are
equal, the shorter sequence is considered smaller: `[1, 2] < [1, 2, 3]` -> `True`. If a pair of
elements does not support ordering (for example, `int` and `str`), a `TypeError` is raised.
Comparing different sequence types (`list` vs `tuple`) also raises `TypeError`.

## Detailed explanation

The mechanism of lexicographic comparison walks the elements of both sequences pair by pair: first
it checks whether the current pair is equal via `__eq__`; if the pair is equal, comparison moves to
the next pair without calling `__lt__`. Only once the first unequal pair is found does the result
of comparing the whole sequence become the result of comparing that specific pair via `__lt__` (or
the corresponding rich comparison method).[^py314-library-stdtypes] This gives a worst case of
O(min(len(a), len(b))) – the walk stops as soon as a divergence is found, and does not necessarily
reach the end of the shorter sequence.

It matters to distinguish `==` from the ordering operators (`<`, `<=`, `>`, `>=`). Equality (`==`)
between sequences of different types, for example `list` and `tuple`, does not raise an exception –
it simply returns `False`, because `==` does not require type compatibility, only pairwise
comparability of elements. `<` between a `list` and a `tuple`, on the other hand, always raises
`TypeError`, regardless of contents, because the sequence type itself is part of the contract of
the ordering operators, not just the elements inside.[^py314-howto-sorting]

This same mechanics underlies how `sorted()` and `list.sort()` compare tuple keys during multi-key
sorting: `(1, 'b') < (1, 'a')` compares the first elements, sees equality, moves on to the second
elements, and compares those instead. If at some step the elements do not support `__lt__` with
each other (for example `int` and `str`), the `TypeError` is raised exactly at the moment that
specific pair is compared, not at the start of the call – so the prefix of the sequences made up of
comparable elements is processed safely.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
