---
id: py-funcs-0017
title: "Why does writing `lambda i=i: i` remove the late-binding problem in a loop, even though default arguments can themselves be a source of bugs?"
description: "Why does writing `lambda i=i: i` remove the late-binding problem in a loop, even though default arguments can themselves be a source of bugs?"
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [lambda-i-i-i]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-faq-programming-why-do-lambdas-defined-in-a-loop-with
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, FAQ: lambdas created in a loop read the variable when they are called, not when they are defined."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Function definitions: default parameter values are evaluated once, when the function definition is executed; None is the usual default for mutable values."
  - source_id: py314-reference-expressions-lambda
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambda
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section lambda: a lambda behaves like a function defined with def and uses the same parameter-list syntax."
  - source_id: py314-faq-programming-why-are-default-values-shared-between
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-are-default-values-shared-between-objects
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, FAQ: default values are created once, and changing a mutable default affects later calls."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#user-defined-functions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section User-defined functions: the __defaults__ attribute holds the default parameter values."
---

## Short answer

**Default arguments are evaluated once, when `def` or `lambda` runs, so `i=i` stores the current value of `i` as a local parameter of each lambda.**[^py314-reference-compound-stmts-function-definitions][^py314-reference-expressions-lambda] Each lambda gets its own parameter `i` with a fixed value, and `f()` returns it. Risk: if the default is a mutable object (for example `[]`), changing it in one call affects all later calls of that function.[^py314-faq-programming-why-are-default-values-shared-between]

## Detailed explanation

Default parameter values are evaluated once, when the function definition is executed, and they are stored in the function's `__defaults__` attribute.[^py314-reference-compound-stmts-function-definitions][^py314-reference-datamodel] A lambda follows the same rule, because it behaves like a function defined with `def`.[^py314-reference-expressions-lambda] The expression `i=i` is therefore evaluated on every iteration: the right-hand `i` is read when the lambda is created, and its value becomes the default of the parameter. The parameter `i` is a local variable of the lambda, so the lambda no longer reads the shared loop variable and holds its own copy of the value.[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with]

The `__defaults__` attribute shows that each lambda has kept its own value:

```python
fixed = [lambda i=i: i for i in range(3)]
print([f() for f in fixed])             # [0, 1, 2]
print([f.__defaults__ for f in fixed])  # [(0,), (1,), (2,)]
```

The same mechanism makes a mutable default shared by all calls: the object is created once, and changes to it persist across calls.[^py314-faq-programming-why-are-default-values-shared-between]

```python
def add(x, bucket=[]):
    bucket.append(x)
    return bucket

print(add(1), add(2))  # [1, 2] [1, 2]: both calls return the same list object
```

The standard way around this is to use `None` as the default and create a new object in the function body, after an explicit check.[^py314-reference-compound-stmts-function-definitions]

This technique has a limit: a default is an ordinary parameter, so a positional argument from the caller overrides it. `list(map(fixed[2], [10, 20]))` returns `[10, 20]`, because `map` passes arguments and they replace the default. So `i=i` is safe for a lambda that is called without arguments; if positional arguments are possible, make the parameter keyword-only: `lambda *, i=i: i`.

**Common mistakes:**
- assuming that `i=i` is evaluated on every call of the lambda, not once when it is created;
- using a mutable default (`[]`, `{}`) as an empty state that accumulates across calls;
- passing a function with defaults to `map` or a callback that passes arguments, and not noticing that the arguments replace the defaults.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
