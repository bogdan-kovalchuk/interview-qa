---
id: cs-algo-0001
title: "What preconditions does binary search need, and why can inserting into a sorted list still be O(n)?"
description: "What preconditions does binary search need, and why can inserting into a sorted list still be O(n)?"
track: cs
section: algorithms
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
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-bisect
    title: "Python 3.14: Library/bisect"
    url: https://docs.python.org/3.14/library/bisect.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L168-L198
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Binary search requires a sorted sequence; `bisect` finds the insertion position in O(log n), but
`list.insert()` shifts elements in O(n).**[^py314-library-collections] The precondition is sorted
input: `bisect_left` and `bisect_right` rely on ordering via `__lt__`. Even though the search
itself is logarithmic, inserting into a `list` still requires shifting up to n elements, so the
total cost of an insertion is O(n).

## Detailed explanation

`bisect` does not check that the input sequence is sorted – that is a contract, not a runtime
check. If the list is not actually sorted, `bisect_left`/`bisect_right` still return some index
without raising, but that index no longer guarantees a correct order after insertion. The only
requirement on elements is a total order via `__lt__`; `bisect` never calls `__eq__` directly, so
a custom class that defines only `__lt__` is already usable for the search.

For duplicates, `bisect_left` returns the position of the first occurrence and `bisect_right` the
position right after the last one; this lets you control the stability of an insertion relative to
equal elements without changing the search algorithm itself.[^py314-library-bisect]

The reason `list.insert()` stays O(n) even after an O(log n) search for the position is the data
structure itself: a Python `list` is a contiguous array of pointers, and inserting in the middle
requires physically shifting every element to the right of the insertion point one slot over in
memory. That cost does not depend on how fast the position was found, even if it was found
instantly. Switching to `collections.deque` does not fix this either: a `deque` gives O(1) append
and pop at both ends, but inserting or removing at an arbitrary middle position is still O(n),
because it is a double-ended queue, not a structure with O(log n) access to an arbitrary middle
position.[^py314-library-collections]

A structure that genuinely gives O(log n) for both search and insertion is a self-balancing
structure with an ordered index (a skip list, or a balanced BST with rank support), not an array
and not a singly linked list: a linked list gives O(1) insertion once the position is known, but
finding that position in it is linear, because it has no random access by index, which binary
search needs to halve the range.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
