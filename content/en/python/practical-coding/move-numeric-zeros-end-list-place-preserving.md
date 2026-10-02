---
id: py-prac-0015
title: "Move numeric zeros to the end of a list in place, preserving the order of the other elements and using O(1) extra space; do not treat `False` as a zero."
description: "Maintain the next non-zero position and swap each retained element into it."
track: python
section: practical-coding
level: middle
type: coding
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-types
  title: 'Python 3.13: Built-in types'
  url: https://docs.python.org/3.13/library/stdtypes.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-builtins
  title: 'Python 3.13: Built-in functions'
  url: https://docs.python.org/3.13/library/functions.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement `move_zeros(values)` in place, moving numeric zeros to the end while preserving the relative order of all other elements, including False.

## Constraints

- Input is a list of built-in int, float or complex values and bool.
- A zero is a non-bool value equal to 0.
- Use O(1) auxiliary references, return None, and preserve zero objects as well.

## Short answer

**Maintain the next non-zero position and swap each retained element into it.** Treat bool separately because False compares equal to zero. This preserves non-zero order and uses a constant number of references.

## Detailed explanation

Before each step, the prefix contains all retained elements already encountered in their original order. The positions between that prefix and the scan position contain only zeros, so a swap cannot disturb an earlier retained element. Python sorting is stable, but sorting is unnecessary and does not meet the constant auxiliary-space requirement. [^py313-types] [^py313-builtins]

## Examples

```python
values = [0, 1, False, 0, 2]
move_zeros(values)
assert values[:3] == [1, False, 2]
assert values[1] is False
```

## Solution

```python
def move_zeros(values):
    position = 0
    for index, item in enumerate(values):
        if isinstance(item, bool) or item != 0:
            values[position], values[index] = values[index], values[position]
            position += 1
```

## Complexity

O(n) comparisons and swaps for n elements, with O(1) auxiliary references. The input list and its objects are reused; only non-zero relative order is guaranteed. [^py313-types] [^py313-builtins]

## Edge cases

Cover False, True, 0.0, complex zero, empty input, all zeros and an already partitioned list.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

values = [0, False, 2, 0.0, True, 3, 0j]
identity = id(values)
assert move_zeros(values) is None and id(values) == identity
assert values[:4] == [False, 2, True, 3]
assert values[0] is False and values[2] is True
assert all(not isinstance(x, bool) and x == 0 for x in values[4:])
for data in ([], [0, 0], [1, 2], [1, 0]):
    before = sorted(map(id, data))
    move_zeros(data)
    assert sorted(map(id, data)) == before
```

## Evaluation guide

### Expected signals

Use identity checks for booleans in tests because list equality alone cannot distinguish False from 0.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would requiring stable zero order change the algorithm?

## Sources

<!-- generated from frontmatter -->
