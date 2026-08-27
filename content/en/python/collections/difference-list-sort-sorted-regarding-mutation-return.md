---
id: py-coll-0003
title: "What is the difference between `list.sort()` and `sorted()` regarding mutation, return value, and the input iterables each allows?"
description: "What is the difference between `list.sort()` and `sorted()` regarding mutation, return value, and the input iterables each allows?"
track: python
section: collections
level: middle
type: comparison
tags: [list-sort, sorted]
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

**`list.sort()` sorts the list in place and returns `None`; `sorted()` returns a new sorted list
and accepts any iterable.**[^py314-library-stdtypes] `sorted()` works with strings, generators,
sets, and so on, while `list.sort()` is only available on `list`. Both methods are guaranteed to
be stable. <span class="warn">`list.sort()` is a bit faster because it does not create a new list
– use it when the original list no longer needs its old order.</span>

## Detailed explanation

Both use Timsort – a hybrid sort that combines insertion sort for short runs with merge sort to
combine already-ordered stretches, so the asymptotics are the same: O(n log n) worst case and
O(n) on already nearly sorted data.[^py314-howto-sorting] The difference is not the algorithm,
but what gets sorted and where the result goes.

`sorted()` accepts any iterable – a generator, a string, a set, dictionary keys – and always
materialises it into a new list first, then sorts that copy in place; the original iterable stays
unchanged (and, if it is a generator, exhausted after one pass). `list.sort()` exists only as a
method on a concrete `list`, because in-place sorting only makes sense for a mutable structure
with random access by index – `tuple` and strings have no such method at all, since they are
immutable.

That `list.sort()` returns `None` instead of the list itself is a deliberate choice: it rules out
a chain like `x = x.sort()`, which looks like it builds a new sorted variable but actually just
overwrites `x` with `None`, destroying the data. By returning `None`, the API explicitly signals
that the operation is a mutation, not the construction of a new value, and the same style is kept
in other in-place methods, such as `list.reverse()` or `list.extend()`.

Performance differs predictably: `list.sort()` does not allocate a new list or copy elements, so
for a large list whose old order is no longer needed, it is a bit faster and more
memory-efficient than `sorted(x)`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
