---
id: py-decor-0001
title: "When is the decorator expression evaluated, and when is the wrapper the decorator returned actually called?"
description: "When is the decorator expression evaluated, and when is the wrapper the decorator returned actually called?"
track: python
section: decorators
level: middle
type: mechanism
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

**The decorator expression is evaluated once when the function is defined, whereas the wrapper returned by the decorator is invoked on each call to the decorated function.**[^py314-glossary-term-decorator] Specifically, `@dec` executes `dec(func)` immediately in the scope where the function is defined and binds the returned wrapper object. The wrapper itself executes only when someone invokes the decorated name. This means heavy setup logic (such as opening a file) runs at decoration time, while per-call logic belongs inside the wrapper.

## Detailed explanation

In Python, the `def` statement is executable code, which means the `@decorator` syntactic sugar is evaluated and applied immediately when the function is defined (definition time), whereas the returned wrapper function executes only when the decorated function is subsequently called (call time).[^py314-reference-compound-stmts-function-definitions] The syntax `@decorator def func(): ...` is direct shorthand for creating the function object followed immediately by the reassignment `func = decorator(func)`.

When a function is defined at the module level, the decorator is called exactly once when the module is imported or executed for the first time. Inside the decorator's outer body, configuration and setup logic executes: registering endpoints in web routing tables, validating signatures, or setting up closures. The callable returned by the decorator is then bound to the original name `func` in the local namespace.

The inner wrapper code, typically decorated with `@functools.wraps`, does not run at definition time at all.[^py314-library-functools-functools-wraps] It remains dormant until someone actively invokes `func(*args, **kwargs)` at runtime, executing on every subsequent call. This distinction establishes a clear separation of concerns across the lifecycle: one-off setup, static validation, or component registration belongs in the decorator body, whereas dynamic parameter validation, timing metrics, or exception handling belongs inside the wrapper.

Demonstration of execution timing at definition time versus call time:

```python
from functools import wraps

def audit(func):
    print(f"1. Decorator applied to '{func.__name__}' at definition time")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"2. Wrapper called for '{func.__name__}' at runtime")
        return func(*args, **kwargs)

    return wrapper

print("Before function definition")

@audit
def greet(name):
    return f"Hello, {name}!"

print("After function definition")

# The wrapper executes only on runtime calls
print(greet("Alice"))
print(greet("Bob"))
```

**Common mistakes and practical consequences:**
- Placing logic that depends on per-invocation arguments or request context in the outer decorator body instead of inside the wrapper: that code runs only once upon import rather than per call.
- Performing expensive I/O operations (network requests, opening database connections) during decorator execution, which drastically slows down module imports or crashes if dependencies are not yet initialized.
- Unintended test side effects: because importing a module executes all top-level decorators, test suites importing modules can accidentally trigger global registrations or external service calls.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
