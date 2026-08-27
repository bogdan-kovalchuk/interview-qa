---
id: cs-algo-0002
title: "When should you choose BFS for graph traversal, and when DFS?"
description: "When should you choose BFS for graph traversal, and when DFS?"
track: cs
section: algorithms
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L416-L436
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**BFS traverses a graph level by level through a queue and finds the shortest path in unweighted
graphs; DFS goes deep through a stack and uses less memory on wide graphs.**[^py314-library-collections]
Choose BFS when you need the shortest path or a level-by-level traversal. Choose DFS for
topological sorting, cycle detection, or when the target is deep and the graph is wide – DFS
memory is O(depth) versus O(width) for BFS.

## Detailed explanation

Both algorithms visit every reachable vertex exactly once, so the asymptotic cost is the same:
O(V + E) on an adjacency list. The difference is the order of the visit, and that order is exactly
what determines which property of the path you get.

BFS keeps a FIFO queue: a vertex leaves the queue in the same order it entered, so the graph
unfolds in "waves" by distance from the start. That is why the first path found to any vertex is
the shortest one by edge count, not by weight. In Python such a queue is typically
`collections.deque`, because `append`/`popleft` are O(1) there; a plain list would cost O(n) to
pop from the front.[^py314-library-collections] The wave structure of BFS also gives multi-source
BFS "for free" – distances from several start vertices at once.

DFS instead commits to one branch all the way down and only backtracks at a dead end, using an
explicit stack or the call stack. DFS memory is bounded by recursion depth, i.e. O(depth): on a
wide, shallow graph that is far cheaper than the BFS frontier, which can hold O(width) vertices at
once. On a graph that is essentially one long chain, though, DFS depth approaches O(V) and the
memory advantage disappears.

DFS traversal order – post-order in particular – underlies topological sorting and strongly
connected component algorithms, and a back edge found during DFS directly reveals a cycle. BFS
does not give you that property directly.

So:

- if you need the shortest distance by edge count or a level-by-level traversal, use BFS;
- if you need a topological order, cycle detection, or the graph is wide with shallow depth, use
  DFS, because its memory scales with depth, not width.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
