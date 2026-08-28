---
id: py-decor-0003
title: "What metadata, introspection, and debugging problems arise if a wrapper does not use `functools.wraps`?"
description: "What metadata, introspection, and debugging problems arise if a wrapper does not use `functools.wraps`?"
track: python
section: decorators
level: middle
type: pitfall
tags: [functools-wraps]
status: published
updated: 2026-09-05
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L247-L278
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Without `functools.wraps`, the decorated function loses `__name__`, `__doc__`, `__qualname__`,
and `__annotations__` – the wrapper function's attributes are substituted instead.**[^py314-glossary-term-decorator]
For example, `example.__name__` becomes `'wrapper'`, and `__doc__` becomes `None`. This breaks
`help()`, stack traces show the wrong name, and tools such as Sphinx generate incorrect
documentation. The fix is to apply `@functools.wraps(func)` to the wrapper.

## Detailed explanation

Without `functools.wraps`, the wrapper function that a decorator returns in place of the original
becomes a new object with its own `__name__`, `__doc__`, `__qualname__`, `__module__`, and
`__annotations__`, and these blank-by-default attributes are exactly what any code inspecting the
decorated function sees.[^py314-glossary-term-decorator]

The reason is how `def wrapper(*args, **kwargs): ...` is defined inside the decorator: it is a
brand-new function, and Python does not copy the metadata of the closed-over function
automatically. `functools.wraps(func)` performs exactly that copy – it transfers the listed
attributes from `func` onto `wrapper` and also sets `wrapper.__wrapped__ = func` as a reference back
to the original.[^py314-library-functools-functools-wraps]

Without that step, introspection breaks at several levels at once. `help(decorated)` shows the
wrapper's docstring (or its absence) instead of the one the caller actually meant to read.
`inspect.signature(decorated)` returns the generic `(*args, **kwargs)` instead of the real
parameters, so static analysis tools and IDE autocomplete never see the true signature.
Documentation generators such as Sphinx render the wrong description for the function.

For debugging the consequence is worse still: stack traces, logging, and profilers all show the
name `wrapper` instead of the name of the function the candidate actually wrote. If the same
decorator is applied to several different functions, all of them look identical in a traceback,
which makes it harder to tell which one actually failed without extra context.

An example of a decorator without `functools.wraps` and its effect on introspection:

```python
def logged(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@logged
def greet(name):
    """Greet a person by name."""
    ...

print(greet.__name__)  # wrapper, not "greet"
print(greet.__doc__)   # None, not "Greet a person by name."
```

**Typical symptoms without `functools.wraps`:**
- `__name__` and `__qualname__` show `wrapper` instead of the function's real name;
- `__doc__` is lost, and `help()` prints an irrelevant or empty summary;
- `__annotations__` disappear, so type checkers and IDEs cannot see the original signature;
- `inspect.signature()` returns `(*args, **kwargs)` instead of the real parameters;
- tracebacks and logs report `wrapper` as the failure site instead of the original function.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
