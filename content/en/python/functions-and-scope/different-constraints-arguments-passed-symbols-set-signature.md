---
id: py-funcs-0001
title: "What different constraints on how arguments may be passed do the `/` and `*` symbols set in the signature `def f(a, /, b, *, c): ...`?"
description: "What different constraints on how arguments may be passed do the `/` and `*` symbols set in the signature `def f(a, /, b, *, c): ...`?"
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [def-f-a-b-c]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-tutorial-controlflow-special-parameters
    title: "Python 3.14: Tutorial/control flow, special parameters"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#special-parameters
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the section on positional-only (/) and keyword-only (*) parameters, with TypeError examples."
---

## Short answer

**`/` separates the positional-only parameters from the rest, and `*` separates the ordinary parameters from the keyword-only ones.**[^py314-reference-compound-stmts-function-definitions] Parameter `a` (left of `/`) can be passed only by position, so `f(a=1)` raises `TypeError`.[^py314-tutorial-controlflow-special-parameters] Parameter `b` (between `/` and `*`) can be passed either way. Parameter `c` (right of `*`) can be passed only by keyword, so `f(1, 2, 3)` raises `TypeError` because the third positional argument has no slot.[^py314-reference-expressions-calls]

## Detailed explanation

The symbols `/` and `*` are not parameters. They are boundaries in the parameter list, and they define how each parameter may be passed: only by position, either way, or only by keyword. Everything before `/` is positional-only. Everything after `*` is keyword-only. Parameters between them accept both forms. The `/` marker has been available since Python 3.8.[^py314-reference-compound-stmts-function-definitions]

For `def f(a, /, b, *, c): ...` this means the following. Parameter `a` cannot be passed by keyword, so `f(a=1, b=2, c=3)` raises `TypeError`.[^py314-tutorial-controlflow-special-parameters] Parameter `b` accepts both forms. Parameter `c` can be passed only by keyword, so `f(1, 2, 3)` raises `TypeError`: after `a` and `b` there is no slot for a third positional argument, and `c` does not accept it by position.[^py314-reference-expressions-calls]

The example checks each rule; the comments show the results:

```python
def f(a, /, b, *, c):
    return a, b, c

print(f(1, 2, c=3))      # (1, 2, 3): a and b by position, c by keyword
print(f(1, b=2, c=3))    # (1, 2, 3): b may also be passed by keyword

try:
    f(a=1, b=2, c=3)     # TypeError: a is positional-only
except TypeError:
    print('TypeError')

try:
    f(1, 2, 3)           # TypeError: c is keyword-only, the third positional argument has no slot
except TypeError:
    print('TypeError')
```

These constraints matter for API design. A parameter that becomes keyword-only stops accepting positional arguments, so existing calls can break. If a function was `def f(a, b)` and became `def f(a, *, b)`, the call `f(1, 2)` starts raising `TypeError`, because the second positional argument no longer has a slot.[^py314-reference-expressions-calls]

**Common mistakes:**
- assuming that a parameter between `/` and `*` can be passed only by position or only by keyword: it accepts both;
- passing by keyword a parameter to the left of `/` and expecting Python to find it by name;
- adding `*` to an existing signature without checking old calls that passed arguments by position.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
