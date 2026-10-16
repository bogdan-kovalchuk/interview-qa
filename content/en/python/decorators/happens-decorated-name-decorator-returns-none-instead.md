---
id: py-decor-0012
title: "What happens to the decorated name if the decorator returns `None` instead of a callable?"
track: python
section: decorators
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
---

## Short answer

**The decorated name is bound to `None`.**[^py314-reference-compound-stmts-function-definitions] The `@decorator` syntax is roughly equivalent to `func = decorator(func)`: whatever value the decorator returns becomes the new value of the name. If the decorator returns `None` (explicitly, or because it has no `return`), calling `foo()` raises `TypeError: 'NoneType' object is not callable` on CPython 3.13 and 3.14.

```python
def bad_decorator(func):
    return None

@bad_decorator
def foo():
    pass

print(type(foo), foo)  # <class 'NoneType'> None

foo()  # TypeError: 'NoneType' object is not callable
```

## Detailed explanation

A decorator is usually a function that returns another function, applied with the `@` syntax.[^py314-glossary-term-decorator] It is applied once, while the `def` statement runs (definition time). The decorator is called with the function object as its only argument, and Python binds the value it returns to the function name instead of the function itself.[^py314-reference-compound-stmts-function-definitions] No check of that value happens at definition time. If the decorator returns `None`, the assignment succeeds without an error, and the name refers to `None` straight away. The error appears at the first use of the name: a call raises `TypeError`, and attribute access, for example `foo.__name__`, raises `AttributeError` (in CPython 3.13 and 3.14).

The most common cause is a decorator that builds a wrapper but forgets to return it:

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f'calling {func.__name__}')
        return func(*args, **kwargs)
    # forgot: return wrapper

@log_calls
def add(a, b):
    return a + b

print(add)            # None
print(callable(add))  # False
add(1, 2)             # TypeError: 'NoneType' object is not callable
```

The line `@log_calls` runs `add = log_calls(add)`, so `add` becomes `None`. The original function can no longer be reached through that name. It can be recovered only if something else still holds a reference to it, for example a variable the decorator saved earlier. The failure shows up where the function is called, not where the decorator was written.

The message depends on the value the decorator returned. If it returns, for example, the number `42`, the call raises `TypeError: 'int' object is not callable`. So `'NoneType' object is not callable` on a decorated function usually means the decorator returned `None` (explicitly, or because it has no `return`).

**Common mistakes:**
- expecting the error to appear during `def`, not on the first call;
- forgetting `return wrapper`, or `return func` in a decorator that only registers the function;
- indenting `return` inside `wrapper` instead of putting it in the decorator body, so the decorator still returns `None`.
