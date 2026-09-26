---
id: py-decor-0005
title: "How does a decorator factory differ from the decorator itself, and at what stage are its arguments processed?"
description: "How does a decorator factory differ from the decorator itself, and at what stage are its arguments processed?"
track: python
section: decorators
level: middle
type: comparison
tags: []
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

**A decorator factory is a function that returns a decorator; its configuration arguments are evaluated once during decoration, and the returned decorator is then applied to the target function.**[^py314-glossary-term-decorator] For example, `@has_perm('view')` first invokes `has_perm('view')` (the factory), which returns the actual decorator that subsequently receives the function. Without a factory, the `@decorator(arg)` syntax is impossible because a standard decorator accepts only a single argument – the callable itself.

## Detailed explanation

A decorator factory is a higher-order function that accepts arbitrary configuration parameters and returns an actual decorator, whereas the decorator itself accepts strictly one argument – the target function or class object to be decorated.[^py314-reference-compound-stmts-function-definitions] This creates a three-tier callable architecture instead of two: the factory produces the decorator, the decorator produces the wrapper, and the wrapper executes the runtime logic.

The processing of factory arguments occurs at function definition time in two distinct evaluation phases. First, Python evaluates the factory call expression `@factory(*args, **kwargs)`, establishing a closure scope that captures the supplied configuration arguments. Next, the resulting callable returned by the factory is immediately called with the newly created function object. The inner `wrapper` returned from this second step, decorated with `@functools.wraps`, is bound to the original name in the enclosing scope.[^py314-library-functools-functools-wraps]

At runtime (call time), the factory configuration arguments are already frozen inside the wrapper's lexical closure. Every subsequent invocation of the decorated function executes the `wrapper`, which has concurrent access to both the call-time arguments (`*args, **kwargs`) and the configuration state captured during Stage 1.

The three tiers of execution (factory, decorator, and wrapper) across definition and call time:

```python
from functools import wraps

def repeat(num_times: int):
    # Stage 1: Factory called with configuration arguments
    print(f"Stage 1: Factory created with num_times={num_times}")

    def decorator(func):
        # Stage 2: Decorator receives the target callable
        print(f"Stage 2: Decorator applied to {func.__name__}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Stage 3: Wrapper executes on each runtime call
            print(f"Stage 3: Running {func.__name__} {num_times} times")
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator

# Definition time: Stage 1 runs, then Stage 2 runs
@repeat(num_times=2)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Call time: Stage 3 runs on every call
greet("Alice")
```

**Common mistakes and pitfalls:**
- Forgetting parentheses when invoking a factory (`@repeat` instead of `@repeat()`): passing the target function into the factory as its configuration parameter causes cryptic `TypeError` exceptions.
- Mutable default arguments in factories: passing default lists or dicts into factory parameters shares mutable state across all functions decorated with that factory.
- Expecting factory arguments to dynamically re-evaluate per call: because factory parameters are closed over at module import/definition time, updating external variables later will not affect wrapper behavior unless the factory explicitly inspects a mutable reference.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
