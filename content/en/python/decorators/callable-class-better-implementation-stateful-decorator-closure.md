---
id: py-decor-0007
title: "When is a callable class a better implementation of a stateful decorator than a closure?"
description: "When is a callable class a better implementation of a stateful decorator than a closure?"
track: python
section: decorators
level: middle
type: comparison
tags: []
status: published
updated: 2026-10-13
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
  - source_id: py314-glossary-term-descriptor
    title: "Python 3.14: Glossary, descriptor"
    url: https://docs.python.org/3.14/glossary.html#term-descriptor
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Definition of a descriptor: an object that defines `__get__()`, `__set__()` or `__delete__()`. It does not describe how decorators bind to methods."
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Descriptor protocol: if an object stored as a class attribute defines `__get__`, attribute access through an instance calls it. An object that defines none of `__get__`, `__set__` or `__delete__` is not a descriptor."
---

## Short answer

**A callable class is the better choice when the decorator's state must be explicitly initialized, reset or checked, or when the logic spans several methods.** For a single counter, a closure with `nonlocal` is simpler. A decorator is a callable invoked with the function as its only argument.[^py314-reference-compound-stmts-function-definitions] A class adds an explicit `__init__`, state attributes for tests, a reset method and `__repr__`. But an instance of such a class is not a descriptor: when it decorates a method, without `__get__` it does not bind to `self`.[^py314-reference-datamodel-invoking-descriptors]

## Detailed explanation

A decorator is a function that returns another function and is usually applied with the `@` syntax.[^py314-glossary-term-decorator] The reference adds that the decorator expression must produce a callable, which is invoked with the function object as its only argument, and that the returned value is bound to the function's name.[^py314-reference-compound-stmts-function-definitions] A closure and a callable class both satisfy this contract, so the difference lies only in where the state lives.

In a closure, the counter is a variable of the enclosing function, which the wrapper changes through `nonlocal`. Reading that state from outside requires an extra binding, for example `wrapper.reset = reset`. In a callable class, the state is an attribute of the instance: `__init__` receives the function and can validate parameters, and `reset()` and `calls` are ordinary attributes available to tests. For a single counter, a closure is shorter and sufficient; the class form pays off when there is more state and more methods.

In both cases the metadata of the original function should be preserved. `functools.wraps` copies `__name__`, `__doc__` and other attributes onto the wrapper; for a class, `functools.update_wrapper(self, func)` has the same effect.[^py314-library-functools-functools-wraps]

The main trap of a callable class is methods. A function is a descriptor, so `s.ping` receives `self` when accessed through an instance.[^py314-reference-datamodel-invoking-descriptors] An instance of a class without `__get__` is not a descriptor, because a descriptor is an object that defines `__get__()`, `__set__()` or `__delete__()`.[^py314-glossary-term-descriptor] If a method is decorated with such a class, `s.ping(1)` calls `__call__` with `1`, and the original function receives that value as `self` and fails with a `TypeError` about the missing argument `x`. The example below contains the fix: `__get__` returns `functools.partial(self, obj)`. The counter in it is shared by all `Service` instances, because it is stored in the decorator, not in `self`.

```python
import functools

class Counted:
    def __init__(self, func):
        self.func = func
        self.calls = 0                         # state lives on the decorator instance
        functools.update_wrapper(self, func)   # copies __name__, __doc__, ...

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

    def __get__(self, obj, objtype=None):      # without this, self is not passed
        if obj is None:
            return self
        return functools.partial(self, obj)

    def reset(self):
        self.calls = 0

class Service:
    @Counted
    def ping(self, x):
        return x

s = Service()
s.ping(1)
s.ping(2)
print(Service.ping.calls)   # 2: the state is shared by all Service instances
Service.ping.reset()
print(Service.ping.calls)   # 0
```

If the counter must be separate for each instance, store it in attributes of `self` rather than in the decorator.

**Common mistakes:**
- assuming a callable class is always better: for a single counter, a closure is shorter and sufficient;
- decorating a method with a class that has no `__get__` and getting a `TypeError`, because `self` is not passed;
- expecting a separate counter per instance when the decorator keeps its state once for the function.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
