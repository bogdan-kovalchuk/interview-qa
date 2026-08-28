---
id: py-syntax-0014
title: "How does the chained comparison `a < b < c` differ from `a < b and b < c` in the number of times the middle operand is evaluated?"
description: "How does the chained comparison `a < b < c` differ from `a < b and b < c` in the number of times the middle operand is evaluated?"
track: python
section: syntax-and-control-flow
level: middle
type: comparison
tags: [a-lt-b-lt-c, a-lt-b-and-b-lt-c]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**In the chained comparison `a < b < c` the middle operand `b` is evaluated only once, whereas in `a < b and b < c` it is evaluated twice (if `a < b` is true).**[^py314-reference-expressions] The two forms are semantically equivalent in result and in short-circuit behaviour (if `a < b` is false, `c` is not evaluated in either case), but the chained comparison avoids re-evaluating `b`, which matters when `b` is an expression with side effects or an expensive computation.

## Detailed explanation

A chained comparison is not shorthand for `and` but a grammar rule of its own. The expression
`a < b < c` expands to `a < b and b < c` with one correction: the middle operand is evaluated
**once**, and its result is used in both comparisons.[^py314-reference-expressions]

As long as the operands are plain names there is no difference. It appears when the middle operand
is a function call: in the `and` form the call happens twice.

```python
def value():
    print('called')
    return 5

1 < value() < 10      # prints 'called' once
1 < value() and value() < 10   # prints 'called' twice - two different calls
```

This matters for more than speed. If the function has a side effect or returns something new on
every call - reads from an iterator, takes the next item of a queue, goes to the network - the `and`
form compares **different** values, and the result can be logically wrong.

Short-circuiting works identically in both forms: if the first comparison is false, the second is
not evaluated and `c` is not touched at all.[^py314-reference-expressions] The chain gives up
nothing relative to `and`.

**What else is worth knowing about chains:**
- the length is not limited to three: `0 <= i < j < len(items)` is a valid expression;
- operators can be mixed, `is`, `in` and `!=` included: `a is not None != b` expands the same way,
  and that is a frequent source of confusion - it does not read the way it looks;
- `a < b > c` is syntactically valid but almost always signals a mistake in intent;
- a chain is not equivalent to comparing tuples: `(a, b) < (c, d)` is a lexicographic comparison, an
  entirely different operation.

The practical conclusion is simple: a chain is more readable and safer wherever the middle operand
is not a plain name, and that is why `0 <= index < len(items)` is the canonical bounds check rather
than a stylistic preference.[^py314-reference-simple-stmts]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
