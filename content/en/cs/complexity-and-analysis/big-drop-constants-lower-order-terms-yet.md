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
  - source_id: clrs-4e
    title: "Introduction to Algorithms, fourth edition"
    url: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
    accessed: 2026-09-08
    kind: book
    version: "4th edition"
    applicability: "Chapter 3 supports asymptotic notation and the treatment of constant factors and lower-order terms."
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
constants and the lower-order terms.**[^clrs-4e] For example, 3n² + 5n + 100
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
the word "infinity" is where the pitfall lives. For example, at n = 1000 the lower-order term
100n = 100,000 outweighs the leading term 0.01n² = 10,000, even though the quadratic term
eventually dominates.

For the same reason, an O(n²) implementation can beat an O(n log n) implementation on a bounded
input range when its operations are much cheaper. Big O only describes eventual growth; it does
not identify the crossover point or account for instruction cost, allocation, cache behavior, or
other implementation details.

So in interviews and in practice, asymptotics should be read as a scaling forecast, not a direct
speed comparison: it answers "how much does the time grow if the input grows tenfold," not
"which option is faster on my data right now." The second question needs profiling or
benchmarking at the real input sizes, not a complexity analysis.[^clrs-4e]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
