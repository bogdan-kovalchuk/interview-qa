---
id: py-syntax-0013
title: "Why does the expression `-3 ** 2` give a different result than `(-3) ** 2`?"
description: "Why does the expression `-3 ** 2` give a different result than `(-3) ** 2`?"
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [3-2]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14"
  flags: []
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

**`-3 ** 2` gives `-9` while `(-3) ** 2` gives `9`, because the `**` operator binds tighter than a unary minus to its left.**[^py314-reference-expressions] That is, `-3 ** 2` is read as `-(3 ** 2)`. Parentheses change the order: `-3` is evaluated first, and only then raised to the power.

```text
>>> print(-3 ** 2)
-9
>>> print((-3) ** 2)
9
```

## Detailed explanation

`**` is the only operator in Python that binds tighter than a unary minus **to its left** but looser
than a unary minus **to its right**. That is a deliberate rule rather than an accident of the
grammar, and it makes the expression asymmetric.[^py314-reference-expressions]

On the left the minus applies to the already computed power: `-3 ** 2` parses as `-(3 ** 2)`, so `9`
first and then the negation. On the right the minus belongs to the exponent: `2 ** -1` is `2` to the
power `-1`, and no parentheses are needed for it.

```python
-3 ** 2       # -(3 ** 2)  = -9
(-3) ** 2     # (-3) * (-3) =  9
2 ** -1       # 0.5 - the unary minus binds tighter on the RIGHT of **
```

The reason for the choice is mathematical notation. In the formula `-x²` the minus traditionally
covers the whole power, and the language reproduces that habit; at the same time a negative exponent
had to be convenient without parentheses.

One more asymmetry that is easy to forget: `**` is right-associative. `2 ** 3 ** 2` is
`2 ** (3 ** 2)`, that is `512`, not `64`. Most other binary operators are left-associative.

**Practical consequences:**
- in formulas with a negative base the parentheses are mandatory: `(-x) ** 2`, or the sign "falls
  out" to the outside;
- when porting a formula from another language it is worth checking its rules - in some languages
  `-3 ** 2` gives `9`;
- an expression with `**` and several levels is better parenthesised explicitly even where the rules
  allow otherwise: right-associativity is rarely kept in mind;
- for a fractional power of a negative base the result becomes complex rather than an error:
  `(-8) ** (1/3)` is not `-2`.

The quick mental check: if the minus stands before the base and is not in parentheses, it is applied
**last**.[^py314-reference-simple-stmts]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
