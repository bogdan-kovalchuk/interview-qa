---
id: py-funcs-0016
title: "Why do all the functions created as `[lambda: i for i in range(3)]` return the same value once the comprehension has finished?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-faq-programming-why-do-lambdas-defined-in-a-loop-with
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: py314-reference-expressions-lambda
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambda
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dictionaries
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
---

## Short answer

**Every lambda captures the same variable `i`, not its value at creation time; after the comprehension finishes, `i` is 2, so each call returns `2`.**[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with]

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]
```

To freeze the current value, use a default argument: `lambda i=i: i`.

## Detailed explanation

A lambda created in a comprehension is a closure, and it does not copy the value of `i` when it is created. It refers to the variable `i` of the enclosing scope through its cell, so the value is read when the lambda is called, not when it is defined. The Python FAQ explains exactly this: the variable is read at call time.[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with]

The comprehension runs in its own implicitly nested scope, so the name `i` does not stay in the enclosing scope: `print(i)` after the comprehension raises `NameError`.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries] All iterations use the same cell, so after the comprehension finishes the cell holds the last value, 2, and every lambda sees 2 through that cell.

To freeze the value, the lambda takes it as a parameter with a default, and the default is computed when the lambda is created:

```python
fixed = [lambda i=i: i for i in range(3)]
print([f() for f in fixed])  # [0, 1, 2]: each lambda has its own parameter i
```

The default rule is the same as for `def`: the value is computed once, when the function definition is executed.[^py314-reference-compound-stmts-function-definitions] A lambda behaves like a function defined with `def`, so the same rule applies to it.[^py314-reference-expressions-lambda] A factory function gives the same effect, for example `def make(n): return lambda: n`, because each call to `make` creates a new cell.

This technique has a limit: a default is an ordinary parameter, so a call that passes an argument overrides it. `fixed[0](99)` returns `99`, and `list(map(fixed[2], [10, 20]))` returns `[10, 20]`. If the lambda must never take positional arguments, make the parameter keyword-only: `lambda *, i=i: i`; then `f(99)` raises `TypeError`.

**Common mistakes:**
- assuming that `[lambda: i for i in range(3)]` yields 0, 1, 2 because the value is supposedly fixed on each iteration;
- adding a default to a lambda that `map` or a callback calls with arguments, and not noticing that the argument replaces the default;
- looking for `i` after the comprehension: the name does not stay in the enclosing scope, so `print(i)` raises `NameError`.
