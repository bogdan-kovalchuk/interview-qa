---
id: py-prac-0008
title: "Implement the sum of integers in an arbitrarily nested list: reject `bool`, raise `TypeError` for other types, and `ValueError` for a cycle in the lists."
description: "Use an explicit stack of list iterators and track active list identities."
track: python
section: practical-coding
level: middle
type: coding
tags: [bool, typeerror, valueerror]
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

Implement `nested_sum(data)` for arbitrarily deep, acyclic nested lists of integers. Reject bool and other types with TypeError, and list cycles with ValueError.

## Constraints

- The root must be a list.
- A shared sublist counts once per occurrence and is not a cycle.
- Use iterative traversal to avoid Python recursion limits; int subclasses except bool are accepted.

## Short answer

**Use an explicit stack of list iterators and track active list identities.** Reject bool before accepting int. Remove an identity when leaving a list so shared sublists remain valid.

## Detailed explanation

Only ancestors on the current path can close a cycle. A global visited set would wrongly reject repeated references; the active set instead mirrors entry and exit. Iterators keep traversal storage proportional to nesting depth, not list width. [^py313-types] [^py313-builtins]

## Examples

```python
assert nested_sum([1, [2, 3]]) == 6
```

## Solution

```python
def nested_sum(data):
    if not isinstance(data, list):
        raise TypeError("root must be list")
    active = {id(data)}
    stack = [(id(data), iter(data))]
    total = 0
    while stack:
        identity, iterator = stack[-1]
        try:
            item = next(iterator)
        except StopIteration:
            active.remove(identity)
            stack.pop()
            continue
        if isinstance(item, bool):
            raise TypeError("bool is not allowed")
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            identity = id(item)
            if identity in active:
                raise ValueError("cycle detected")
            active.add(identity)
            stack.append((identity, iter(item)))
        else:
            raise TypeError("unsupported leaf")
    return total
```

## Complexity

O(v) traversal operations and O(d) auxiliary references for v visited occurrences and maximum depth d, assuming expected constant-time set operations. Big-integer addition costs and the accumulator bytes are additional; repeated shared subtrees count repeatedly. [^py313-types] [^py313-builtins]

## Edge cases

Test self-cycles, indirect cycles, repeated shared lists, invalid leaves and depth beyond the recursion limit.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

assert nested_sum([]) == 0
assert nested_sum([1, [2, [-3]], []]) == 0
shared = [2, 3]
assert nested_sum([shared, shared]) == 10
cycle = []
cycle.append(cycle)
with pytest.raises(ValueError):
    nested_sum(cycle)
a, b = [], []
a.append(b)
b.append(a)
with pytest.raises(ValueError):
    nested_sum(a)
for invalid in (True, 1.0, "1", (1,), None):
    with pytest.raises(TypeError):
        nested_sum([invalid])
with pytest.raises(TypeError):
    nested_sum(1)
deep = [7]
for _ in range(2000):
    deep = [deep]
assert nested_sum(deep) == 7
```

## Evaluation guide

### Expected signals

Distinguish an active ancestor from a previously visited list. Do not solve arbitrary depth with recursive calls.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would you bound work on heavily shared input graphs?

## Sources

<!-- generated from frontmatter -->
