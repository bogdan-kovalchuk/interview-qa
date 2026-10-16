---
id: py-funcs-0020
title: "How does passing `handler` differ from passing `handler()` as an argument to a higher-order function?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-datamodel-objects-values-and-types
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#objects-values-and-types
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
  - source_id: py314-reference-expressions-lambdas
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambdas
---

## Short answer

**`handler` passes the function object itself (a callable) that the higher-order function can call later; `handler()` calls the function immediately and passes its result.**[^py314-reference-datamodel-objects-values-and-types] A common mistake is `register(handler())`, which registers whatever `handler` returns rather than the function itself. If `handler` returns `None`, `None` is registered.

## Detailed explanation

The difference lies in what the expression contains: the function's name or its call. The expression `handler` gives the function object itself, a reference to an object that can be called at any later time. The expression `handler()` is a call: Python runs the function first, and its result becomes the argument value. All argument expressions are evaluated before the call is attempted.[^py314-reference-expressions-calls] So in `register(handler())`, `handler()` runs first, and only then does `register` receive whatever it returned.

A higher-order function sees only the finished argument value. It expects a callable and will call it at its own time. If it receives a result instead of a callable, the failure does not appear where the mistake was made, but later, when someone tries to call the stored value.

The example shows both forms. The call `register(on_start)` stores the function object and prints nothing. The call `register(on_start())` runs the function immediately, so `started` is printed during registration and `None` is stored:

```python
handlers = []

def register(callback):
    handlers.append(callback)

def on_start():
    print("started")

register(on_start)      # stores the function object, prints nothing
register(on_start())    # prints "started" now, stores None
print([type(h).__name__ for h in handlers])  # ['function', 'NoneType']

try:
    for h in handlers:
        h()             # the first call prints "started"; calling None fails
except TypeError as e:
    print("TypeError:", e)  # TypeError: 'NoneType' object is not callable
```

The failure is deferred: the loop calls the stored objects, and `None` cannot be called, so execution fails with `TypeError`, even though the wrong call was made earlier in a different place.

If the handler needs arguments, `register(handler(42))` again runs the function immediately. To defer a call with an argument, pass `lambda: handler(42)`. The lambda is itself a function object, and it calls `handler` with the argument only when the higher-order function calls it.[^py314-reference-expressions-lambdas]

**Common mistakes:**
- writing `register(handler())` instead of `register(handler)`: registration succeeds without an exception, so the mistake is easy to miss;
- thinking `handler()` only passes the function along: in fact the function runs right there and then;
- passing `handler(42)` where a deferred call is needed; use `lambda: handler(42)` instead.
