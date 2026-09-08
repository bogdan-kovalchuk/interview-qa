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
  - source_id: clrs-4e
    title: "Introduction to Algorithms, fourth edition"
    url: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
    accessed: 2026-09-08
    kind: book
    version: "4th edition"
    applicability: "Chapter 14 supports memoization, bottom-up dynamic programming, and state-based complexity analysis."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
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

**Memoization or bottom-up dynamic programming avoids recomputing overlapping subproblems by
solving each reachable state once.**[^clrs-4e] The resulting time is approximately the number of
reachable states times the transition cost, so it is polynomial only when that state space and
transition work are polynomial. For Fibonacci, this changes exponential recursion to O(n) time
and O(n) memo storage.

## Detailed explanation

Naive recursion over a problem with overlapping subproblems builds a call tree whose size depends
on the number of *paths* to each state, not on the number of states themselves. For Fibonacci
there are only n + 1 states, but the call tree has size O(2^n), because each state fib(k) is
recomputed once for every recursive path that leads to it.

Memoization folds that tree back into a graph: before computing a state, the code checks a table,
and if the state is already there, it returns the stored value instead of descending again. When
a state is described by several parameters, it is reduced to a hashable key – a tuple or, for
readability, a namedtuple.[^py314-library-collections] Each unique state is then computed exactly
once, and the total time becomes O(number of reachable states × transition cost excluding
recursive calls) – O(n) for Fibonacci instead of O(2^n).[^clrs-4e]

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

Both approaches remove duplicated evaluation of the same state, but they do not guarantee a
polynomial algorithm: a problem can still have exponentially many distinct reachable states. The
trade-off between them is recursion with demand-driven evaluation versus iteration with the option
to compress memory.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
