---
id: py-decor-0002
title: "In what order are two decorators, `@outer` and `@inner`, written above the same function, applied?"
description: "In what order are two decorators, `@outer` and `@inner`, written above the same function, applied?"
track: python
section: decorators
level: middle
type: mechanism
tags: [outer, inner]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L3-L79
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Decorators are applied bottom to top: first `@inner`, then `@outer`, which is equivalent to
`func = outer(inner(func))`.**[^py314-glossary-term-decorator] Each subsequent decorator receives
the result of the previous one.

```python
def outer(func):
    print('outer applied')
    return func

def inner(func):
    print('inner applied')
    return func

@outer
@inner
def hello(): pass
```

Output at definition time: `inner applied`, then `outer applied`.

## Detailed explanation

Applying a decorator means calling its function immediately when the `def` statement executes
(definition time), not later when the decorated function itself is called. Python processes a stack
of decorators over one function bottom to top: the one closest to `def` runs first, and only its
result is passed to the next one.[^py314-glossary-term-decorator]

This follows directly from the syntax: `@outer` `@inner` `def hello(): ...` is shorthand for
`hello = outer(inner(hello))`, and Python evaluates the nested calls from the inside out, so
`inner(hello)` is evaluated first.[^py314-reference-compound-stmts-function-definitions] Each
subsequent decorator receives the already-wrapped function as its argument, never the original.

The order of *application* (who wraps whom at definition time) is worth separating from the order
of *execution* at call time. If each wrapper does something before and after calling the next
function, then on a call `outer`'s code runs first (because it is outermost), then `inner`'s code,
then the original function, and on the way back the order reverses. This is the same call-stack
behaviour as any nested function, and it is exactly where it is easiest to confuse "which decorator
was applied first" with "whose code runs first".

An example that shows the difference between application order and execution order:

```python
def outer(func):
    def wrapper(*args, **kwargs):
        print('outer: before')
        result = func(*args, **kwargs)
        print('outer: after')
        return result
    return wrapper

def inner(func):
    def wrapper(*args, **kwargs):
        print('inner: before')
        result = func(*args, **kwargs)
        print('inner: after')
        return result
    return wrapper

@outer
@inner
def hello():
    print('hello')

hello()  # order: outer:before, inner:before, hello, inner:after, outer:after
```

**Common mistakes with decorator order:**
- assuming the order of writing does not matter as long as the decorators "just log something";
- confusing application order (bottom to top, once at definition time) with wrapper execution order
  (on every call, outermost first);
- reordering decorators during refactoring without checking whether that breaks behaviour that
  depended on who wraps whom.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
