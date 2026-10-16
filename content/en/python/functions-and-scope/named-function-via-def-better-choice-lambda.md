---
id: py-funcs-0021
title: "When is a named function via `def` a better choice than a `lambda`, even when both can implement the same short expression?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-expressions-lambdas
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambdas
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: pep-8
    title: "PEP 8: Style Guide for Python Code"
    url: https://peps.python.org/pep-0008/#programming-recommendations
---

## Short answer

**`def` is the better choice when you need a meaningful name for tracebacks, a docstring, type annotations, or several statements in the body.**[^py314-reference-expressions-lambdas] A lambda is limited to one expression and cannot contain statements or annotations.[^py314-reference-expressions-lambdas] Its `__name__` is `"<lambda>"` by default, which makes diagnostics harder.[^pep-8] A `def` creates a function object with its own name, which appears in tracebacks.

## Detailed explanation

A lambda and a `def` create objects of the same kind: both give a function object that can be called, passed as a callback, or stored in a variable. The difference lies in the syntax and in what can be expressed. A lambda is an expression that, according to the documentation, behaves like a function object defined with `def <lambda>(parameters): return expression`. So its body is a single expression, with no statements, annotations or docstring.[^py314-reference-expressions-lambdas]

A name matters when the function must be recognized outside the code: in a traceback, in a repr, in logs. A `def` defines a user-defined function object and binds it to a name.[^py314-reference-compound-stmts-function-definitions] A lambda, even when assigned to a variable, keeps the generic name `<lambda>`, so a call stack does not show which function failed:

```python
def normalize_price(value: str) -> float:
    """Convert a price string to cents."""
    return float(value) * 100

as_lambda = lambda value: float(value) * 100

print(normalize_price.__name__)          # normalize_price
print(as_lambda.__name__)                # <lambda>
print(normalize_price.__annotations__)   # {'value': <class 'str'>, 'return': <class 'float'>}
print(normalize_price.__doc__)           # Convert a price string to cents.
print(as_lambda.__doc__)                 # None
```

A failure inside either function gives a traceback line `in normalize_price` for a `def` and `in <lambda>` for a lambda. This is why PEP 8 explicitly recommends a `def` over binding a lambda directly to an identifier: the function then has a real name rather than the generic `<lambda>`.[^pep-8] A shorter form is not a reason to use a lambda when the function must be reused, documented or diagnosed.

**Common mistakes:**
- assuming that a lambda and a `def` differ only in notation: a lambda cannot contain several statements, annotations or a docstring;
- assigning a lambda to a variable and expecting a real name in the traceback, when it will show `<lambda>`;
- choosing a lambda only for its shorter form when the function must be reused or diagnosed.
