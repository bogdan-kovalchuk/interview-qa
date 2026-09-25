---
id: py-coll-0005
title: "How does a tuple containing a mutable element behave when `t[0] += value` is attempted, and why can the mutation happen before the `TypeError`?"
description: "How does a tuple containing a mutable element behave when `t[0] += value` is attempted, and why can the mutation happen before the `TypeError`?"
track: python
section: collections
level: senior
type: pitfall
tags: [t-0-value, typeerror]
status: published
updated: 2026-09-27
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
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Applying `+=` to a mutable element inside a tuple first performs an in-place mutation and then attempts to assign the result back to the tuple slot – the assignment raises `TypeError`, but the mutation has already occurred.**[^py314-library-stdtypes]

```text
t = ([1, 2], [3])
t[0] += [3]    # TypeError, but t[0] is already [1, 2, 3]
```

The expression `t[0] += [3]` effectively executes `t[0] = t[0].__iadd__([3])`: `__iadd__` mutates the list, and then `tuple.__setitem__` rejects the assignment.

## Detailed explanation

The paradox of the expression `t[0] += [3]` on a tuple stems from the fact that augmented assignment decouples into two distinct steps: an in-place mutation of the referenced object followed by reassigning the resulting reference back to the container slot.[^py314-library-stdtypes]

At the CPython bytecode level, the statement `target[index] += value` emits an operation sequence that loads the object from the slot, applies `INPLACE_ADD` (invoking the `__iadd__` method), and subsequently attempts to persist the returned reference via `STORE_SUBSCR`.[^py314-library-stdtypes] For a `list`, `__iadd__` mutates the list in-place (equivalent to `extend()`) and returns `self`. The mutation succeeds immediately, but the subsequent `STORE_SUBSCR` instruction invokes `tuple.__setitem__`, which unconditionally raises `TypeError: 'tuple' object does not support item assignment` because tuples are immutable.

This behavior violates transactional atomicity: the operation fails with a runtime exception while leaving behind a mutated, half-updated state. This represents a fundamental architectural design trade-off in Python: the runtime does not implement rollback mechanisms when composite operations raise exceptions. When in-place mutation is required, engineers should either use a `list` as the outer container, avoid mutable elements inside tuples altogether, or invoke explicit mutating methods like `t[0].extend(...)` which do not perform an assignment back to the tuple slot.

Demonstrating augmented assignment failure and non-atomic mutation:

```python
# 1. Setup a tuple holding a mutable list:
t = ([1, 2], [3])

# 2. Augmented assignment causes an in-place mutation followed by TypeError:
try:
    t[0] += [3]
except TypeError as exc:
    print(exc)  # 'tuple' object does not support item assignment

# The list inside the tuple was mutated before the exception was raised:
print(t[0])  # [1, 2, 3]

# 3. Explicit method call mutates without attempting tuple item assignment:
t[1].extend([4])
print(t[1])  # [3, 4]
```

**Architectural implications and common mistakes:**
- assuming that an operation raising an exception guarantees the original state is preserved (Python provides no implicit rollback);
- embedding mutable objects (`list`, `dict`) inside tuples, breaking the guarantee of immutability and rendering the tuple unhashable;
- confusing an explicit mutating method like `lst.extend(...)` (which leaves the tuple untouched) with `+=` (which requires reassigning the slot);
- wrapping `t[0] += value` in a `try/except TypeError` block as a hacky way to mutate, which creates fragile, anti-pattern control flow.

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
