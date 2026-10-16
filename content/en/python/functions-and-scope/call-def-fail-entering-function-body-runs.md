---
id: py-funcs-0002
title: "When and why does the call `f(1, a=2)` for `def f(a): ...` fail: before entering the function body, or while it runs?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
---

## Short answer

**A `TypeError` about multiple values for `a` is raised before the function body is entered, during argument binding.**[^py314-reference-expressions-calls] The positional argument `1` fills the slot of parameter `a`, and the keyword `a=2` tries to fill the same slot. The interpreter checks for such conflicts while matching arguments to parameters, so the body never runs.

## Detailed explanation

The call happens in two stages: first Python matches the arguments to the parameters, and only then the function body runs. For `def f(a): ...`, the positional `1` fills the slot `a`, and the keyword `a=2` targets that same slot. The documentation describes this as part of argument processing: if the slot is already filled, a `TypeError` is raised; otherwise the argument is placed in the slot, and once all arguments are processed the filled slots become the argument list for the call.[^py314-reference-expressions-calls]

The example shows the difference: the print in the body happens only if the body has started running:

```python
def f(a):
    print('body runs')
    return a

try:
    f(1, a=2)                # TypeError at binding: 'body runs' is not printed
except TypeError:
    print('TypeError')

def g(a):
    print('body runs')
    return len(a)

try:
    g(5)                     # 'body runs' is printed, then TypeError inside the body
except TypeError:
    print('TypeError')
```

Argument expressions are evaluated before Python attempts the call. So side effects in the arguments happen even if the call then fails with `TypeError`. The documentation says so directly: all argument expressions are evaluated before the call is attempted.[^py314-reference-expressions-calls]

It is important to tell apart two cases: a `TypeError` raised while matching arguments, and a `TypeError` raised from inside the body, such as `len(a)` in `g(5)`. The wording of the message differs between the documentation's examples and CPython 3.13, so rely on behaviour instead: whether the first line of the body ran.

**Common mistakes:**
- looking for the cause in the function body when the body has not run yet;
- assuming that argument expressions are not evaluated when the call fails;
- missing a conflict between a positional argument and a `**` unpacking: `f(1, **{'a': 2})` raises the same error.[^py314-reference-expressions-calls]
