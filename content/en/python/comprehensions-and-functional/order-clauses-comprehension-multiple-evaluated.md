---
id: py-compfn-0002
title: "In what order are the clauses of a comprehension with multiple `for` and `if` evaluated?"
description: "In what order are the clauses of a comprehension with multiple `for` and `if` evaluated?"
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
---

## Short answer

**Clauses are evaluated left to right, like nested loops: each `for` is a new nesting level, and
`if` filters at the current level.**[^py314-howto-functional] The result is equivalent to nested
`for`/`if` blocks left to right, where the result expression is evaluated every time execution
reaches the deepest level. For example, `[(i,j) for i in range(3) for j in range(2) if (i+j) % 2 ==
0]` gives `[(0, 0), (1, 1), (2, 0)]`.

## Detailed explanation

The order of `for`/`if` clauses in a comprehension directly determines at what stage filtering
happens, not just the semantics of the result. The compiler translates a comprehension into a
sequence of nested loops literally: each subsequent `for` compiles as the body of the previous one,
so a variable bound by the first `for` is visible to every `for` and `if` to its right, but no `for`
can see variables that are bound later.[^py314-reference-expressions-displays-for-lists-sets-and-dict]

Where an `if` sits in the chain affects the number of iterations performed, not only what ends up in
the result. If an `if` sits right after `for x`, it prunes unsuitable `x` values before entering the
nested loop over `y` – elements that fail the condition never trigger any iteration of the inner
loop at all. Move that same `if` to the very end, after both `for` clauses, and the outer and inner
loops still run to completion for every pair, with filtering happening only at the deepest level.
The result is identical either way, but the number of iterations performed – and therefore the cost
when the `for` sources are expensive – is not.

Several consecutive `if` clauses at the same level (with no `for` between them) behave as a
short-circuited sequence of conditions, equivalent to `if cond1 and cond2`: if `cond1` is false,
`cond2` is never evaluated. That matters when the second condition could raise an exception on
elements the first condition has already filtered out – the order of the `if` clauses is then a
deliberate choice, not an arbitrary one.

The result expression itself (written before the first `for`) is not evaluated once for every
combination up front; it is evaluated each time execution reaches the deepest nesting level and
every `if` along that path has passed – exactly like the body of the innermost loop in equivalent
explicit code.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
