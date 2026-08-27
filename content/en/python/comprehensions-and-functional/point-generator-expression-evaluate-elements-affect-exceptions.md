---
id: py-compfn-0005
title: "At what point does a generator expression evaluate its elements, and how does that affect exceptions and side effects?"
description: "At what point does a generator expression evaluate its elements, and how does that affect exceptions and side effects?"
track: python
section: comprehensions-and-functional
level: middle
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
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md#L19-L28
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A generator expression creates the iterator immediately, but evaluates each element only when
`next()` is called (lazy evaluation).**[^py314-howto-functional] This means exceptions and side
effects are deferred until consumption time, rather than occurring when the expression is created.
For example, `g = (1/x for x in data)` does not raise `ZeroDivisionError` until the first `next(g)`
that reaches the element `x == 0`.

## Detailed explanation

The key asymmetry: only the iterable expression of the very first (outermost) `for` is evaluated
immediately – `iter()` is called on it right away when the generator is created, before the first
`next()`.[^py314-howto-functional] Everything else – the iterable expressions of later `for`
clauses, the `if` conditions, and the result expression itself – is evaluated only lazily, one
element at a time, during iteration. So `(x for x in get_items())` calls `get_items()` immediately
when the expression is created, but the contents it returns are processed only incrementally.

This has a practical consequence for side effects and exceptions: if the generator is never fully
iterated (say, a loop `break`s early, or the generator is simply discarded), the elements execution
never reaches are never evaluated, and no side effects or exceptions occur for them. That is what
distinguishes a generator expression from a list comprehension, where the whole result is
materialized immediately, so every side effect and every exception happens right away, in element
order, before the comprehension returns a list.

Another difference is single use: a generator expression is an iterator, and once fully consumed
(`StopIteration`), it is exhausted for good; iterating the same object again with another `for`
yields nothing. A list comprehension, by contrast, produces a new list that can be iterated as many
times as needed.

For nested `for` clauses inside a generator expression, the lazy behavior extends to the inner
iterable expressions too: the iterable expression of an inner `for` is evaluated freshly on every
iteration of the outer one, not computed once up front – exactly as in ordinary nested loops, just
with deferred execution.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
