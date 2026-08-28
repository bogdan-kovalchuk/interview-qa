---
id: py-syntax-0001
title: "Do the `and` and `or` operators always return a `bool`, or one of their own operands, and how does short-circuit evaluation work?"
description: "Do the `and` and `or` operators always return a `bool`, or one of their own operands, and how does short-circuit evaluation work?"
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [and, or, bool]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L3-L20
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`and` and `or` return one of their operands, not necessarily a `bool`.**[^py314-reference-expressions] `x and y` evaluates `x`: if `x` is falsy it returns it, otherwise it returns `y`. `x or y` evaluates `x`: if `x` is truthy it returns it, otherwise it returns `y`. Short-circuiting means the second operand is not evaluated once the first has settled the result.

## Detailed explanation

`and` and `or` are not boolean operators in the sense of "returning `True`/`False`" but selection
operators: they return **the operand** that settled the result, in its original
form.[^py314-reference-expressions]

One rule covers both. `x or y` evaluates `x`; if it is truthy that is the result, and `y` is not
evaluated at all. `x and y` evaluates `x`; if it is falsy the result is `x`, and again `y` is not
evaluated.

```python
0 or 'default'      # 'default' - the str, not True
'a' or 'b'          # 'a'       - the first truthy operand
[] and crash()      # []        - crash() is never called
1 and 2             # 2         - the last operand, because 1 is truthy
```

Truthiness is decided by the object itself through `__bool__`, or through `__len__` in its absence;
the result therefore depends on the operand's type rather than on some universal
coercion.[^py314-reference-simple-stmts]

Short-circuiting is a guarantee of the language, not an optimisation, and can be relied on. That is
why the idiom `obj is not None and obj.value > 0` works: if the first part is false the attribute is
never read, and no `AttributeError` occurs.

**Practical consequences worth naming:**
- a default via `or` replaces any falsy value, not just `None` - the classic trap with `0` and `''`;
- the chain `a or b or c` returns the first truthy operand, and if all are falsy the **last** one,
  not `False`;
- annotating the result as `bool` is wrong: the result type is the union of the operand types;
- if a `bool` is what you need, say so explicitly: `bool(x or y)`;
- side effects in the second operand may not happen - that is the whole point of short-circuiting,
  and guard checks are built on it.

Separately, `and`/`or` should not be confused with `&`/`|`: the latter are bitwise operators, they
do not short-circuit, and for ordinary objects they mean something else
entirely.[^py314-reference-expressions]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
