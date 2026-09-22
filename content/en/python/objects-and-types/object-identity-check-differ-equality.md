---
id: py-objtypes-0001
title: "How does an object-identity check with `is` differ from equality with `==`?"
description: "How does an object-identity check with `is` differ from equality with `==`?"
track: python
section: objects-and-types
level: middle
type: comparison
tags: [is]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L587-L609
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`is` checks object identity (the exact same object in memory), while `==` checks value equality.**[^py314-reference-datamodel] The `is` operator compares the `id()` of objects and cannot be overloaded. The `==` operator invokes the `__eq__()` method; if a class does not define its own `__eq__`, the default `object.__eq__` falls back to `is`.

## Detailed explanation

The `is` operator determines whether two variables reference the exact same object in memory, whereas the `==` operator checks whether the values of the objects are equivalent.[^py314-reference-datamodel]

In CPython, every object has an immutable identity, a type, and a value. The built-in `id()` function returns an integer representing the object's address in memory. The `is` operator directly compares object pointers at the C-structure level. This operation runs in $O(1)$ time, invokes no Python methods, and cannot be overloaded by user code.

In contrast, the `==` operator delegates evaluation to the `__eq__()` special method of the left operand. If that method returns `NotImplemented`, the interpreter attempts to call `__eq__()` on the right operand. If neither operand defines an equality comparison, Python falls back to `object.__eq__`, which defaults to an identity check using `is`.[^py314-library-stdtypes] User-defined classes can freely override `__eq__` to compare specific attributes or apply custom equality semantics.

An example demonstrating the distinction between identity and value equality:

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True: values are equal
print(a is b)  # False: distinct objects in memory with different id()
print(a is c)  # True: c references the exact same object as a

print(id(a) == id(b))  # False: id() comparison matches the result of `is`
```

**Common mistakes and practical consequences:**
- comparing numbers or strings using `is` instead of `==`: due to interning optimizations in CPython this may coincidentally evaluate to `True`, but it is not guaranteed by the language specification;
- assuming `==` always returns a `bool`: objects in specialised libraries may return complex structures or raise exceptions;
- overlooking performance differences: `is` is always instantaneous, whereas `==` on large nested collections recursively traverses every element.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
