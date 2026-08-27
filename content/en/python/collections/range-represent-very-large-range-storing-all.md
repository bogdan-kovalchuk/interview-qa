---
id: py-coll-0002
title: "Why can `range` represent a very large range without storing all the integers in memory?"
description: "Why can `range` represent a very large range without storing all the integers in memory?"
track: python
section: collections
level: middle
type: mechanism
tags: [range]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L406-L428
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`range` stores only three values – `start`, `stop`, `step` – and computes elements on demand, so
it uses O(1) memory regardless of the range's size.**[^py314-library-stdtypes] `range(10**15)`
and `range(10)` occupy the same amount of memory. Both `in` (an arithmetic check) and indexing run
in O(1).

## Detailed explanation

`range` is not a container of elements but a compact description of an arithmetic progression: the
object stores only three numbers (`start`, `stop`, `step`) and a formula for computing the i-th
element – `start + i * step`.[^py314-library-stdtypes] That is exactly why `range(10**15)` and
`range(10)` are created instantly and occupy the same, fixed amount of memory: the size of the
range does not affect the size of the object itself, because no element is ever materialised in
advance.

This is what sets `range` apart from a generator, which is also lazy but can only move forward
sequentially and does not know its own length up front. `range` implements `__len__`,
`__getitem__`, and `__contains__` directly via arithmetic, so `range(10**15)[500]` is computed in
O(1) by a plain substitution into the formula, not by stepping through 500 intermediate values.
The membership check `x in r` is also O(1): it only needs to verify that `x` lies within
`[start, stop)` and that `(x - start) % step == 0`, with no iteration at all.

Iterating (`for i in range(...)`) creates a separate `range_iterator`, which on each step simply
adds `step` to the current value – O(1) per element, O(n) for the whole pass, but without keeping
previous values: the memory needed for iteration does not depend on how many elements have already
been produced.

Slicing (`range(...)[a:b:c]`) does not materialise anything either – the result of a slice is a
new `range` object with recomputed `start`/`stop`/`step`, not a list of elements, so even taking a
slice of a billion-element `range` is an O(1) operation. If you do convert a `range` into
`list(range(10**15))`, Python will genuinely try to allocate memory for each element separately,
and that will predictably fail with `MemoryError` long before disk space runs out.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
