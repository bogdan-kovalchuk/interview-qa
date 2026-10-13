---
id: py-prac-0003
title: "What does `a = [[1]]; b = a.copy(); b[0].append(2); print(a)` print, and how does a shallow copy create this aliasing bug?"
description: "It prints [[1, 2]]: list.copy() copies only the outer list, so a and b share the inner list."
track: python
section: practical-coding
level: middle
type: pitfall
tags: [a-1-b-a-copy-b-0-append-2-print-a]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, copy module: assignment does not copy an object; list.copy() and copy.copy() make a shallow copy that inserts references to the original's elements; copy.deepcopy() copies nested objects recursively."
---

## Short answer

**It prints `[[1, 2]]`: `a` also sees the change.** `list.copy()` makes a shallow copy: a new outer list that holds the same elements, so a nested list is copied only by reference.[^py314-library-copy] Therefore `b[0]` and `a[0]` are the same `list` object, and `append(2)` through `b` changes it for both. <span class="warn">For a copy that does not share nested objects, use `copy.deepcopy()`.[^py314-library-copy]</span>

## Detailed explanation

The assignment `b = a` does not copy the list: it only adds another name for the same object.[^py314-library-copy] The method `a.copy()` creates a different outer list, but it does not copy the elements. That is a shallow copy: a new container whose references point to the same objects as the original.[^py314-library-copy]

The expression `b[0] is a[0]` shows the shared object. A mutation through `b[0]` is visible through `a`, because the inner list itself changes, not a reference inside the outer list:

```python
a = [[1]]
b = a.copy()
print(b[0] is a[0])  # True: both lists share the same inner object
b[0].append(2)
print(a)  # [[1, 2]]
b.append(3)
print(a)  # [[1, 2]]: the outer list is independent
```

The aliasing here goes only one level deep. Adding an element to the outer `b` does not change `a`, because the outer lists are different. That is why the bug is easy to miss: a test that changes only the top level passes, while a change to a nested element breaks the original.

If the nested objects must be independent, use `copy.deepcopy()`. It copies nested objects recursively and keeps a memo dictionary of objects already copied, so recursive structures do not cause an endless traversal.[^py314-library-copy] Example:

```python
import copy

a = [[1]]
c = copy.deepcopy(a)
c[0].append(2)
print(a)  # [[1]]
print(c)  # [[1, 2]]
```

A deep copy is not always right either: it may copy data that was meant to stay shared between the copies.[^py314-library-copy]

**Common mistakes:**
- assuming that `list.copy()` makes a full copy of nested structures;
- changing a nested element in one copy and expecting the other one to stay the same;
- using `copy.deepcopy()` everywhere, even when the data was meant to be shared.

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
