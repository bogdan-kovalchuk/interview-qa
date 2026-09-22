---
id: py-objtypes-0006
title: "How does in-place mutation of a list via `+=` differ from augmented assignment for an immutable tuple?"
description: "How does in-place mutation of a list via `+=` differ from augmented assignment for an immutable tuple?"
track: python
section: objects-and-types
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L48-L93
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**For `list`, the `+=` operator invokes `__iadd__` and mutates the list in-place (preserving its `id`); for `tuple`, there is no `__iadd__` method, so it falls back to `__add__`, which creates a new tuple.**[^py314-reference-datamodel] After `t += (3,)` on a tuple, the name `t` is rebound to a new object with a different `id()`. For a list, `lst += [3]` expands the existing object with new elements.

## Detailed explanation

The augmented assignment operator `x += y` in Python operates through a special method protocol where the presence of the `__iadd__` method plays the decisive role.[^py314-reference-datamodel]

For mutable types like `list`, the `__iadd__` method is implemented to perform an in-place mutation of the internal array of pointers and return `self`. The operation `lst += iterable` is functionally equivalent to `lst.extend(iterable)` – the right-hand operand can be any iterable, not just a list. The target variable is then rebound to the exact same object, meaning its `id()` remains identical and all existing references observe the mutation.

In contrast, immutable types such as `tuple` do not implement `__iadd__` in order to preserve the invariant that an object cannot change after creation.[^py314-library-stdtypes] When `__iadd__` is absent, the interpreter falls back to binary addition `x = x + y`, calling `tuple.__add__`. This method strictly requires the right-hand operand to be another `tuple`, allocates a new tuple in memory, and copies references from both operands into it. The variable name is then rebound to this newly created tuple, while the original tuple remains untouched.

A notable edge case occurs when attempting `+=` on a mutable element inside a tuple, such as `nested[0] += [3]`. The augmented assignment executes in two steps: first, the list's `__iadd__` runs and successfully mutates the list in place, but subsequently the bytecode attempts to store the returned reference back into `nested[0]`, raising a `TypeError` because tuples do not permit item assignment.

An example demonstrating the behavioral difference and the nested mutable element edge case:

```python
# List: in-place mutation via __iadd__ (same object ID)
lst1 = [1, 2]
lst2 = lst1
lst1 += [3, 4]
print(lst1 is lst2)  # True, both references see the mutation

# Tuple: creates a new object via __add__ fallback (different ID)
tup1 = (1, 2)
tup2 = tup1
tup1 += (3, 4)
print(tup1 is tup2)  # False, tup1 rebound to a newly created tuple

# Subtle pitfall: mutating a list inside a tuple via +=
nested = ([1, 2],)
try:
    nested[0] += [3]
except TypeError:
    print(nested)  # ([1, 2, 3],) - in-place mutation succeeded before assignment failed
```

**Common mistakes and practical implications:**
- expecting `t += (x,)` to modify an existing tuple in-place, which inside loops leads to quadratic complexity due to repeated memory allocations;
- passing a list into a function and using `+=` instead of `+`, inadvertently mutating the caller's list;
- forgetting that the right operand for `list += ...` can be any iterable (for instance, `lst += "ab"` appends individual characters `['a', 'b']` rather than the string as a whole);
- falling into the `nested_tuple[0] += [item]` trap, where a `TypeError` is raised even though the list inside the tuple was actually mutated.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
