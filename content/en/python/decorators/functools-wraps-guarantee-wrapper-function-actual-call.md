---
id: py-decor-0004
title: "What does `functools.wraps` not guarantee about the wrapper function's actual call signature?"
description: "What does `functools.wraps` not guarantee about the wrapper function's actual call signature?"
track: python
section: decorators
level: senior
type: mechanism
tags: [functools-wraps]
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

**`functools.wraps` copies only metadata attributes (`__name__`, `__doc__`, `__qualname__`, `__annotations__`, `__type_params__`) and sets `__wrapped__`, but does not alter the actual call signature of the wrapper function.**[^py314-glossary-term-decorator] The wrapper remains a function defined with its own parameters (typically `*args, **kwargs`). While `inspect.signature()` unwraps `__wrapped__` by default to display the original signature, the underlying callable still accepts whatever parameters the wrapper defines – meaning argument mismatch errors only occur when arguments are processed inside the wrapper or forwarded to the wrapped function.

## Detailed explanation

The `functools.wraps` decorator performs strictly metadata mutations via `functools.update_wrapper`: it copies the attributes `__name__`, `__doc__`, `__qualname__`, `__annotations__`, and `__type_params__`, while attaching a `__wrapped__` reference pointing to the original callable.[^py314-library-functools-functools-wraps] Fundamentally, `functools.wraps` alters neither the wrapper's underlying code object (`__code__`) nor Python's argument-binding rules: the actual calling signature remains exactly what was declared for the `wrapper` function (typically `*args, **kwargs`).

Although `inspect.signature()` unwraps the `__wrapped__` chain by default (`follow_wrapped=True`) to reflect the wrapped target's signature, this is an intentional illusion at the inspection layer.[^py314-reference-compound-stmts-function-definitions] At CPython's virtual machine level, dispatch occurs against the wrapper's actual parameters. If a caller supplies missing required arguments or invalid keyword arguments, the invocation is not rejected at the entry boundary. Any preamble code in the wrapper (such as acquiring locks, logging, or opening transactions) runs immediately, and a `TypeError` only surfaces when execution eventually reaches the forwarded `func(*args, **kwargs)` call.

Furthermore, `functools.wraps` provides no guarantees for static type systems (mypy, pyright), which inspect AST definitions rather than runtime attribute mutations. Without explicit use of `typing.ParamSpec` and `typing.Concatenate` in modern Python, decorating a function causes type checkers to lose original parameter constraints or collapse the callable into `Callable[..., Any]`.

Demonstrating the divergence between the actual callable signature and the unwrapped representation:

```python
import inspect
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapper entered before argument verification")
        return func(*args, **kwargs)
    return wrapper

@log_call
def multiply(x: int, y: int) -> int:
    return x * y

# inspect.signature follows __wrapped__ by default
print(inspect.signature(multiply))  # (x: int, y: int) -> int
print(inspect.signature(multiply, follow_wrapped=False))  # (*args, **kwargs)

# Calling with invalid arguments still executes the wrapper preamble
try:
    multiply()  # missing arguments: x and y
except TypeError as error:
    print(f"Caught expected error: {error}")
```

**Architectural trade-offs and pitfalls:**
- False assumptions about early parameter validation: side effects in the wrapper preamble (such as metrics increments or distributed trace spans) execute even if invalid arguments cause the wrapped call to fail with `TypeError`.
- Dependency injection friction in frameworks (e.g., FastAPI, pytest): libraries inspecting callable parameters or accessing raw code objects may encounter subtle mismatches between inferred parameters and actual forwarded values.
- Pre-execution validation requires explicitly calling `inspect.signature(func).bind(*args, **kwargs)` inside the wrapper before running any preamble logic.
- Static typing safety requires typing decorators with `ParamSpec` and a generic `Callable[P, R]` return type rather than relying solely on runtime `functools.wraps`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
