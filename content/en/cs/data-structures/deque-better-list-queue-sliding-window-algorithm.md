---
id: cs-dstruct-0002
title: "When is `deque` better than `list` for a queue or a sliding-window algorithm?"
description: "When is `deque` better than `list` for a queue or a sliding-window algorithm?"
track: cs
section: data-structures
level: middle
type: comparison
tags: [deque, list]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/data_structures.md#L367-L398
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`deque` gives O(1) for append and pop at both ends, while `list` costs O(n) for `pop(0)` or
`insert(0, v)`, because the elements have to be shifted in memory.**[^py314-library-collections]
For a FIFO queue or a sliding-window algorithm that adds/removes elements at the front,
`collections.deque` avoids that linear cost. Use `list` when append/pop are only needed at the
end (a stack) or when you need O(1) access by index.

## Detailed explanation

`collections.deque` is implemented as a doubly linked list of fixed-size blocks (not of
individual elements), so each block holds several pointers in a row – this gives better cache
locality than a classic singly linked list, and at the same time O(1) amortized cost for
`append`, `appendleft`, `pop`, `popleft`, because adding or removing at an edge never requires
shifting other elements.

`list`, by contrast, is a contiguous array of pointers. `append`/`pop` at the end are O(1)
amortized (Python occasionally over-allocates the array), while `pop(0)`/`insert(0, v)` require
physically shifting every other element one slot over, i.e. O(n).

This directly explains why `deque` is the natural choice for sliding-window algorithms: the
classic example is finding the maximum in every window of size k (a `monotonic deque`), where
elements are simultaneously added at the right edge and removed at the left, and a deque keeps
both O(1). Implementing the same pattern with a `list` would cost O(n) per removal from the
front, i.e. O(n*k) overall instead of O(n).

The price for this advantage is losing random access by index: `deque[i]` for an `i` in the
middle is O(n), because you have to walk the blocks sequentially from the nearest edge, whereas
`list[i]` is always O(1), since it is a directly computed offset into a contiguous array.
Likewise, slicing (`deque[a:b]`) is not supported as efficiently natively as `list[a:b]`.

So the choice is a trade-off: if the algorithm mainly works at the ends of the sequence (a
queue, a stack, a sliding window), `deque` is the better fit; if you need frequent random access
by index or slicing, `list` remains the better choice, even when it occasionally needs an
insertion at the front.[^py314-library-collections]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
