---
id: py-decor-0006
title: "How do you design a decorator with two distinct call forms, `@trace` and `@trace(level=2)`, without confusing the decorated callable with configuration arguments?"
description: "How do you design a decorator with two distinct call forms, `@trace` and `@trace(level=2)`, without confusing the decorated callable with configuration arguments?"
track: python
section: decorators
level: senior
type: practical
tags: [trace, trace-level-2]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Inspect whether the first argument is callable: if `func is not None`, it is the bare `@trace` form, otherwise return a partial decorator with the bound configuration.**[^py314-glossary-term-decorator] A standard pattern defines the outer function as `trace(func=None, *, level=1)`. When `func` is provided as a callable, apply the wrapper immediately; when `None`, return a configured decorator closure. An alternative is `functools.partial` or a dedicated factory class. Crucially, configuration arguments must be keyword-only to prevent a passed configuration value from being mistaken for a callable.

## Detailed explanation

Supporting both calling styles (`@trace` without parentheses and `@trace(level=2)` with arguments) is elegantly achieved by combining an optional first positional parameter `func=None` with keyword-only parameters (`*`) for all configuration options.[^py314-reference-compound-stmts-function-definitions] The bare `@trace` syntax passes the decorated function as the first positional argument, whereas `@trace(level=2)` invokes the decorator without positional arguments, leaving `func` as `None`.

The critical architectural design decision is deliberately avoiding type checks such as `callable(arg)`. If any configuration parameter can itself be a callable (such as a custom validator, error predicate, or serializer), positional dispatch creates an unresolvable ambiguity where the decorator mistakes a configuration callback for the decorated target function. Enforcing keyword-only arguments (`*`) after `func=None` eliminates this ambiguity at the grammar level: callers cannot inadvertently pass configuration into the `func` positional slot.

When `func is None`, the function behaves as a decorator factory and returns a partially applied version of itself via `functools.partial(trace, level=level)` or an equivalent closure.[^py314-library-functools-functools-wraps] When that returned callable subsequently receives the target function, it executes `trace(func, level=level)`, returning the wrapper protected by `@functools.wraps`. This pattern also inherently supports empty parentheses (`@trace()`) without requiring specialized branches.

Implementing a dual-form decorator using keyword-only parameters and `functools.partial`:

```python
from functools import partial, wraps

def trace(func=None, *, level=1):
    """Decorator supporting both @trace and @trace(level=2) forms."""
    if func is None:
        # Called with arguments or empty parentheses: return a configured decorator
        return partial(trace, level=level)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TRACE L{level}] Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

# Form 1: Bare decorator without parentheses
@trace
def add(a, b):
    return a + b

# Form 2: Parametrized decorator with keyword arguments
@trace(level=2)
def multiply(a, b):
    return a * b

# Form 3: Empty parentheses with default configuration
@trace()
def subtract(a, b):
    return a - b

add(2, 3)       # [TRACE L1] Calling add
multiply(2, 3)  # [TRACE L2] Calling multiply
subtract(5, 2)  # [TRACE L1] Calling subtract
```

**Architectural trade-offs and pitfalls:**
- Allowing positional configuration arguments: defining `def trace(func=None, level=1)` causes `@trace(2)` to bind `2` to `func`, triggering runtime failures when Python attempts to call the integer.
- Relying on `callable(func)` without keyword-only constraints: if a decorator accepts a function as configuration (e.g. `@retry(predicate=is_transient)`), positional passing erroneously routes into the bare decorator branch.
- Empty parenthesis handling: invoking `@trace()` must return the configured decorator without errors, which is handled cleanly by the `func is None` check.
- Static typing ergonomics: to maintain full IDE auto-completion and static analysis under mypy or pyright, dual-form decorators should define `@typing.overload` signatures separating the bare callable form from the parameterized factory form.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
