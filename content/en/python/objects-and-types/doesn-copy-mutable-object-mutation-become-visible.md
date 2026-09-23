---
id: py-objtypes-0005
title: "Why doesn't `y = x` copy a mutable object, and how does a mutation through `y` become visible through `x`?"
description: "Why doesn't `y = x` copy a mutable object, and how does a mutation through `y` become visible through `x`?"
track: python
section: objects-and-types
level: middle
type: mechanism
tags: [y-x]
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
---

## Short answer

**Assignment `y = x` copies only the object reference, not the object itself; both names point to the exact same mutable object.**[^py314-reference-datamodel] Any mutation made through one name (such as `y.append(3)` on a list) is immediately visible through the other because `x` and `y` reference the same memory address. Creating an independent duplicate requires `copy.copy()` or `copy.deepcopy()`.

## Detailed explanation

In Python, variables are not memory locations that store values directly, but rather symbolic names or references bound to objects allocated on the heap.[^py314-reference-datamodel]

The assignment statement `y = x` evaluates the expression on the right-hand side and binds the name `y` to the exact same object already referenced by `x`, incrementing its reference count. The underlying object is neither duplicated nor moved. Both variables share the identical memory address (`id(x) == id(y)`), and the identity test evaluates to `x is y == True` (aliasing).

When an object belongs to a mutable type (such as `list`, `dict`, or `set`), mutating operations (such as `.append()` or in-place index assignment) modify its internal state in place without creating a new object. Because `x` points to the same underlying heap memory, inspecting the object through `x` immediately reflects any mutations performed through `y`.[^py314-library-stdtypes]

To prevent unintended shared mutations, an independent copy must be created explicitly. A shallow copy (`copy.copy()`, the `.copy()` method, or slicing `[:]`) allocates a new outer container but retains references to the original nested elements. If the data structure contains nested mutable objects, robust isolation requires a deep copy via `copy.deepcopy()`, which recursively duplicates every level of the hierarchy.[^py314-library-copy]

An example illustrating the difference between reference aliasing, shallow copying, and deep copying:

```python
import copy

x = [1, [2, 3]]
y = x                  # Aliasing: both names reference the exact same object
shallow = copy.copy(x) # Shallow copy: new outer list, but shared inner list
deep = copy.deepcopy(x) # Deep copy: independent duplicate of all nested objects

y[0] = 99
y[1].append(4)

print(x)        # [99, [2, 3, 4]]: in-place mutations through y are seen in x
print(shallow)  # [1, [2, 3, 4]]: outer list preserved, but nested list was mutated
print(deep)     # [1, [2, 3]]: completely isolated from mutations
```

**Common traps and practical recommendations:**
- mutable default arguments in functions: `def fn(items=[]):` constructs a single list when the function is defined, causing subsequent calls to mutate the shared instance;
- creating nested lists via sequence multiplication: `matrix = [[0] * 3] * 3` produces an outer list with three references to the exact same inner list;
- relying on shallow copies for nested structures: `x[:]` duplicates only the top-level container, leaving nested lists or dictionaries shared;
- unintended side effects: passing a mutable object to a function permits in-place modifications that alter the caller's state without an explicit return statement.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
