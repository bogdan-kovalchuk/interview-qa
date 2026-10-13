---
id: py-funcs-0004
title: "How does Python bind the arguments in the call `f(1, 2, 3, b=4, x=5)` to the parameters of `def f(a, *args, b=0, **kwargs): ...`?"
description: "How does Python bind the arguments in the call `f(1, 2, 3, b=4, x=5)` to the parameters of `def f(a, *args, b=0, **kwargs): ...`?"
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [f-1-2-3-b-4-x-5, def-f-a-args-b-0-kwargs]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`a = 1`, `args = (2, 3)`, `b = 4`, `kwargs = {'x': 5}`.**[^py314-reference-expressions-calls] The first positional argument fills parameter `a`. The following positional arguments `2, 3` have no matching parameters before `*`, so they are collected into `*args`. The keyword `b=4` matches the keyword-only parameter `b`. The keyword `x=5` matches no named parameter and goes into `**kwargs`.

## Detailed explanation

Python matches arguments to parameters in two steps. First, positional arguments fill the positional parameters in order: `a` receives `1`. Excess positional arguments that have no slot are collected into a tuple for `*args`. Then each keyword argument looks for a parameter with the same name: `b=4` fills the keyword-only `b`, and `x=5` has no such parameter, so it goes into `**kwargs`.[^py314-reference-expressions-calls] A parameter after `*`, such as `b`, can be filled only by keyword.[^py314-reference-compound-stmts-function-definitions]

The example has three calls; the comments show the results:

```python
def f(a, *args, b=0, **kwargs):
    return a, args, b, kwargs

print(f(1, 2, 3, b=4, x=5))   # (1, (2, 3), 4, {'x': 5})
print(f(1, 2, 3, 4))          # (1, (2, 3, 4), 0, {}): b is keyword-only, so 4 goes to *args
print(f(a=1, x=5))            # (1, (), 0, {'x': 5}): a can also be passed by keyword
```

Two consequences are worth remembering. First, `b` is keyword-only, so the positional `4` in the second call goes to `*args`, not to `b`. Second, a keyword whose name matches a named parameter does not go into `**kwargs`: in the third call, `a=1` fills `a`.[^py314-reference-expressions-calls] If `a` is already filled by position, as in `f(1, a=2)`, a `TypeError` is raised; see `qid:py-funcs-0002`.

**Common mistakes:**
- expecting the positional `4` in `f(1, 2, 3, 4)` to become the value of `b`: `b` is reachable only by keyword;
- assuming that a keyword whose name matches a parameter ends up in `**kwargs`;
- assuming that an empty `*args` is `None`: it is always a tuple, `()`, and an empty `**kwargs` is `{}`.[^py314-reference-expressions-calls]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
