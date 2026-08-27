---
id: cs-dstruct-0001
title: "For a stream of jobs, when should you choose a hash table for lookup by ID, and when a min-heap for repeatedly extracting the lowest priority?"
description: "For a stream of jobs, when should you choose a hash table for lookup by ID, and when a min-heap for repeatedly extracting the lowest priority?"
track: cs
section: data-structures
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/data_structures.md#L85-L154
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`dict` gives O(1) average-case complexity for lookup by key; a min-heap built on `heapq` gives
O(log n) for push/pop and O(1) for peeking at the smallest element.**[^py314-library-collections]
Choose a hash table when the main operation is looking up or updating a job by its unique ID.
Choose a min-heap when you need to keep extracting the job with the lowest priority – a heap
does not support O(1) arbitrary lookup by ID.

## Detailed explanation

The two structures have fundamentally different internal organization. `dict` is a hash table: a
key is hashed, and the hash computes a direct index into an internal array, so lookup, insertion,
and deletion by key are O(1) on average (worst case O(n) under massive collisions, which is rare
in practice thanks to the quality of the hash function). But `dict` does not support ordered
access – "find the minimum" would require an O(n) pass over all the values.

`heapq` implements a min-heap as a plain `list`, where for index `i` the children live at
indices `2i+1` and `2i+2`; this implicit tree structure guarantees that `heap[0]` is always the
minimum, and `heappush`/`heappop` restore the invariant by sifting (`sift up`/`sift down`) in
O(log n). But a heap does not index elements by an arbitrary key: checking whether a job with a
given ID is already in the heap, or updating its priority, needs a linear O(n) pass – the data
structure simply does not record where a specific element sits.

That is exactly why, for a stream of jobs that needs both operations – fast lookup by ID and
repeatedly extracting the lowest priority – the typical solution combines both structures: a
`dict` maps an ID to a record (job, priority, a validity flag), while `heapq` stores the same
records as `(priority, id)` tuples. Priority updates are implemented via lazy deletion: the old
entry in the heap is marked invalid (for example, by keeping a separate "live" record in the
`dict`) instead of removing it from the middle of the heap at O(n) cost, and `heappop` skips
invalid entries until it finds the actual minimum.[^py314-library-heapq]

This hybrid – a classic "indexed priority queue" – gives O(log n) for push/pop-min and O(1) for
lookup by ID, at the cost of somewhat more bookkeeping for entry validity.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
