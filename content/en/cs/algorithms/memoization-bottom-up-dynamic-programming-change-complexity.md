---
id: cs-algo-0003
title: "How does memoization or bottom-up dynamic programming change the complexity of a recursive solution with overlapping subproblems?"
description: "How does memoization or bottom-up dynamic programming change the complexity of a recursive solution with overlapping subproblems?"
track: cs
section: algorithms
level: senior
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L516-L530
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Memoization or bottom-up dynamic programming reduces a recursion with exponential time and
overlapping subproblems to polynomial time, by solving each unique subproblem only
once.**[^py314-library-collections] For example, naive recursive Fibonacci has O(2^n) complexity,
but with a memo table each of the n subproblems is computed once – giving O(n) time and O(n)
memory. The trade-off is extra memory for the cache instead of repeated computation.

## Detailed explanation

Naive recursion over a problem with overlapping subproblems builds a call tree whose size depends
on the number of *paths* to each state, not on the number of states themselves. For Fibonacci
there are only n + 1 states, but the call tree has size O(2^n), because each state fib(k) is
recomputed once for every recursive path that leads to it.

Memoization folds that tree back into a graph: before computing a state, the code checks a table,
and if the state is already there, it returns the stored value instead of descending again. When
a state is described by several parameters, it is reduced to a hashable key – a tuple or, for
readability, a namedtuple.[^py314-library-collections] Each unique state is then computed exactly
once, and the total time becomes O(number of states × cost of a transition excluding recursive
calls) – O(n) for Fibonacci instead of O(2^n).

Bottom-up DP reaches the same result a different way: instead of recursing top-down, it builds the
table bottom-up, in an order that guarantees that when state k is computed, every state it depends
on is already filled in. For Fibonacci that is simply increasing index order; for harder problems
it is a topological order over the dependencies between states.

The difference between the two approaches is not in time complexity, but in exactly which states
get computed and what the overhead structure costs:

- top-down memoization computes only the states actually needed for the answer, but pays for a
  call stack of depth O(depth), which can hit Python's recursion limit;
- bottom-up tabulation computes every state in the range, even ones not needed for a given query,
  but avoids recursion, and if a state depends on only a constant number of earlier ones (as
  Fibonacci depends on two), the table can be collapsed to fixed-size variables – O(1) memory
  instead of O(n).

So both approaches remove the exponential duplication of work, turning the problem from O(2^n)
into O(number of unique states); the trade-off between them is recursion with lazy evaluation
versus iteration with the option to compress memory.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
