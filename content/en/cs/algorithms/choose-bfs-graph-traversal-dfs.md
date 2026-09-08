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
  - source_id: clrs-4e
    title: "Introduction to Algorithms, fourth edition"
    url: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
    accessed: 2026-09-08
    kind: book
    version: "4th edition"
    applicability: "Chapters 20-22 support BFS/DFS complexity, shortest paths in unweighted graphs, and DFS applications."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
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
graphs; DFS goes deep through a stack and can keep a smaller frontier on wide, shallow
graphs.**[^clrs-4e]
Choose BFS when you need the shortest path or a level-by-level traversal. Choose DFS for
topological sorting or depth-oriented exploration. For graph traversal, both algorithms can also
need an O(V) visited set; only their queue or stack frontier has the familiar O(width) versus
O(depth) contrast.

## Detailed explanation

With a visited set, both algorithms process every reachable vertex and edge a constant number of
times, so the asymptotic cost is O(V + E) on an adjacency list.[^clrs-4e] The difference is the
visit order, and that order determines which path properties are available.

BFS keeps a FIFO queue: a vertex leaves the queue in the same order it entered, so the graph
unfolds in "waves" by distance from the start. That is why the first path found to any vertex is
the shortest one by edge count, not by weight. In Python such a queue is typically
`collections.deque`, because `append`/`popleft` are O(1) there; a plain list would cost O(n) to
pop from the front.[^py314-library-collections] The wave structure of BFS also gives multi-source
BFS "for free" – distances from several start vertices at once.

DFS instead commits to one branch all the way down and only backtracks at a dead end, using an
explicit stack or the call stack. Its active path can be O(depth), while a BFS queue can grow to
O(width). This comparison excludes the visited set required for a general graph, which can be O(V)
for either traversal. An iterative DFS can also hold multiple pending neighbors, so O(depth) is not
a universal total-memory bound for every implementation.

DFS traversal order – post-order in particular – underlies topological sorting and strongly
connected component algorithms.[^clrs-4e] In a directed graph, a back edge found by DFS reveals a
cycle; in an undirected graph, the edge to the parent must be excluded from that test.

So:

- if you need the shortest distance by edge count or a level-by-level traversal, use BFS;
- if you need a topological order or depth-oriented exploration, use DFS; on a wide, shallow graph
  its active frontier can be smaller than BFS's, but count the visited set separately.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
