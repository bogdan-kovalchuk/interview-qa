---
id: py-coll-0020
title: "What does the stability of Python's sort mean, and how can it be used for multi-key sorting without a custom comparator?"
description: "What does the stability of Python's sort mean, and how can it be used for multi-key sorting without a custom comparator?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L292-L321
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Stability means that elements with an equal key keep their original relative order; that is what lets you sort by several keys in sequence, from the least significant to the most significant.**[^py314-library-stdtypes] For example, to sort by `grade` descending and `age` ascending: first `sorted(data, key=age)`, then `sorted(result, key=grade, reverse=True)`. Stability guarantees that the order by `age` survives within an equal `grade`. The alternative, when one direction suffices, is a tuple key: `key=itemgetter(grade, age)`.

## Detailed explanation

Stability is a property of a particular sorting algorithm, not an abstract guarantee of the notion
of "sorting": `sorted()` and `list.sort()` in CPython are implemented with Timsort, a hybrid merge
sort which, when merging two sorted runs, always takes the element from the left run if the keys are
equal, and never swaps elements with an equal key.[^py314-howto-sorting] It is that property of the
algorithm, not the language documentation, that makes the sequential-sort trick correct.

The correctness of the sequential approach rests on induction: after sorting by the least
significant key the elements are ordered by it. The next sort by a more significant key groups the
elements by the new key, but because it is stable, within each group of an equal new key the order
established by the previous sort is not disturbed. Repeating that from the least significant key to
the most significant yields a correct multi-key order without writing a comparator of your own.

The trick is especially useful when different keys need opposite directions (one ascending, another
descending), because the tuple-key approach (`key=itemgetter(a, b)`) sorts both fields in the one
direction given by the single `reverse`. For numeric fields the direction can be inverted by
replacing the key with `-value`, but for string fields there is no such direct trick - and that is
exactly where sequential `sorted()` calls with a separate `reverse` per key beat the tuple key.

The limit of the approach: it needs as many passes as there are keys, that is O(k * n log n) instead
of a single O(n log n) for the tuple-key variant - acceptable for a few keys, not for many.[^py314-library-stdtypes]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
