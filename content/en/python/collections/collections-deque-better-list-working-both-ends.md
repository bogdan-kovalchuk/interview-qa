---
id: py-coll-0023
title: "When is `collections.deque` better than a list for working at both ends of a sequence?"
description: "When is `collections.deque` better than a list for working at both ends of a sequence?"
track: python
section: collections
level: middle
type: comparison
tags: [collections-deque]
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
---

## Short answer

**`deque` guarantees O(1) append and pop at both ends, while `list` requires O(n) for
`insert(0, v)` and `pop(0)` because elements have to shift in the
array.**[^py314-library-stdtypes] That makes `deque` better for queues, sliding windows, and
algorithms that need efficient work at both ends. <span class="warn">At the same time, `deque` has
O(n) access to the middle by index, so for random access `list` remains the better
choice.</span>

## Detailed explanation

Internally, `deque` is a doubly linked list of fixed-size blocks (each block holds a few dozen
elements), not a list of separate per-element nodes and not a contiguous
array.[^py314-library-collections] This block-based design gives amortized O(1) for `append`,
`appendleft`, `pop`, and `popleft`, because adding or removing usually touches only one block at
the edge of the structure, without moving any other elements.

`list.append()` is also amortized O(1) thanks to over-allocated memory at the end of the array,
but operations at the left edge – `insert(0, v)` and `pop(0)` – are always O(n), because `list`
physically shifts every element to keep the array contiguous in memory; the block structure of
`deque` needs no such shift.

The price for this is random access by index: `d[i]` on a `deque` requires walking from the
nearest edge (left or right) through the blocks, i.e. O(n) in the worst case, while `list[i]` is
always O(1), because the array gives a direct memory offset.

The `maxlen` parameter makes `deque` a convenient ring buffer for a sliding window: once the
length reaches `maxlen`, every new `append` automatically evicts an element from the opposite end
without an explicit `popleft` call.

One more practical detail – `append`/`pop` at opposite ends of a `deque` in CPython are atomic at
the GIL level, so for the simplest producer-consumer scenarios between two threads a `deque`
needs no extra locking; `list` does not document the same guarantee as explicitly for operations
at both ends.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
