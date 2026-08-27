---
id: cs-cmplx-0003
title: "Why does Big O drop constants and lower-order terms, yet they still matter for real input sizes?"
description: "Why does Big O drop constants and lower-order terms, yet they still matter for real input sizes?"
track: cs
section: complexity-and-analysis
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L156-L161
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Big O describes the growth rate as n -> infinity, when the dominant term outweighs the
constants and the lower-order terms.**[^py314-library-collections] For example, 3n² + 5n + 100
simplifies to O(n²), because the quadratic term dominates for large n. However, for real, finite
inputs, the constant factor and the lower-order terms determine actual running time – an O(n²)
algorithm with a small constant can outperform O(n log n) at practical values of n.

## Detailed explanation

The formal definition f(n) = O(g(n)) means there exist constants c > 0 and n0 such that
f(n) <= c*g(n) for all n >= n0. This inequality deliberately ignores the actual value of c: the
asymptotics describe a growth class, not the running time on a specific processor. That is why
500n and n both fall into the class O(n), even though the 500x difference is entirely real on
any input.

The reason lower-order terms vanish is the same: as n -> infinity, the ratio of a lower-order
term to the dominant term goes to zero, so it becomes negligible next to the leading term. But
the word "infinity" is where the pitfall lives: for a concrete n = 1000, a term like 100n can
outweigh n² if the quadratic term has a small coefficient while the constant 100 does not.

In practice this shows up as follows: insertion sort, O(n²), with a very small inner constant (a
simple loop with no function calls, good cache locality) regularly beats merge sort, O(n log n),
on arrays up to a few dozen or a few hundred elements – which is exactly why real-world
implementations (the `sort` routine in many languages) fall back to insertion sort below some
threshold. Big O only guarantees which algorithm wins asymptotically once n is large enough; it
says nothing about how large that n has to be.

So in interviews and in practice, asymptotics should be read as a scaling forecast, not a direct
speed comparison: it answers "how much does the time grow if the input grows tenfold," not
"which option is faster on my data right now." The second question needs profiling or
benchmarking at the real input sizes, not a complexity analysis.[^py314-library-collections]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
