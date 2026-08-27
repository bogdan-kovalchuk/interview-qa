---
id: cs-cmplx-0002
title: "What is the time complexity of the code `for i in range(n): for j in range(i): work()`, and what sum explains it?"
description: "What is the time complexity of the code `for i in range(n): for j in range(i): work()`, and what sum explains it?"
track: cs
section: complexity-and-analysis
level: middle
type: mechanism
tags: [for-i-in-range-n-nbsp-nbsp-for-j-in-range-i-work]
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

**The time complexity is O(n²), explained by the triangular sum 0 + 1 + 2 + ... + (n-1) =
n(n-1)/2.**[^py314-library-collections] The inner loop runs `i` times for each `i` from 0 to
n-1, which sums to n(n-1)/2 calls to `work()`. Verified on Python 3.14: n=10 -> 45 calls, n=100
-> 4950 calls. The constant factor of 1/2 is dropped in Big O notation.

## Detailed explanation

The sum 0 + 1 + ... + (n-1) follows from the classic Gauss trick: if you write the same sum in
reverse order and add term by term, every pair of terms gives the same value n-1, and there are
n such pairs. So the doubled sum equals n*(n-1), and the sum itself is n(n-1)/2. This is the
triangular number formula, which describes the number of unique unordered pairs among n
elements – which is exactly why this same loop pattern shows up in all-pairs comparison problems
(such as a naive duplicate check or O(n²) sorting).

It matters to distinguish the exact number of calls to `work()`, which equals n(n-1)/2, from the
asymptotic class O(n²): the formula is exact for any n, while Big O only describes that the
growth is quadratic, dropping the factor of 1/2 and the lower-order term. If the inner loop were
`range(n)` instead of `range(i)`, the exact call count would be n², but the complexity class
would remain the same O(n²) – the only difference is a constant factor of two.

This asymmetry of the loops (the inner range depends on the outer variable) does not change the
overall complexity class compared to a symmetric double loop `range(n)` x `range(n)`, because in
both cases the number of iterations is proportional to n². But it matters in practice: the actual
number of operations is half as many, so this code runs roughly twice as fast as a full double
pass over n x n, even with identical asymptotics.[^py314-library-collections]

Generalizing to k nested loops with a similarly shrinking range gives complexity O(n^k / k!) –
the combinatorial count of k-element subsets, another example of how the nesting structure of
loops maps directly onto a formula from combinatorics.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
