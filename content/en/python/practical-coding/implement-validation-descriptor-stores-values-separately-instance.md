---
id: py-prac-0020
title: "Implement a validation descriptor that stores values separately for each instance and works with two managed attributes."
description: "Record a private attribute name in __set_name__ and store values on the owning instance."
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
- source_id: py313-descriptor
  title: 'Python 3.13: Descriptor guide: managed attributes and validators'
  url: https://docs.python.org/3.13/howto/descriptor.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-model
  title: 'Python 3.13: Data model: hashing and context managers'
  url: https://docs.python.org/3.13/reference/datamodel.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement `Validated(validator)` using the descriptor protocol. Support two managed attributes and keep their values separate across instances.

## Constraints

- Use one descriptor object per managed attribute.
- Owners have an instance __dict__ and reserve the private storage names.
- Validators raise on invalid input.
- Class access returns the descriptor; an unset instance attribute raises AttributeError.

## Short answer

**Record a private attribute name in `__set_name__` and store values on the owning instance.** Validate before assignment so failed writes preserve the previous value. Return the descriptor itself for class-level access.

## Detailed explanation

The descriptor belongs to the class, so storing a current value on it would share state. Separate private names isolate the two fields while instance storage isolates objects. Reserving the private names and avoiding descriptor reuse are explicit limits of this simple design. [^py313-descriptor] [^py313-model]

## Examples

```python
# A validator that accepts any value.
class Record:
    value = Validated(lambda value: None)
r = Record()
r.value = 8
assert r.value == 8
```

## Solution

```python
class Validated:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.storage_name = "_validated_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        self.validator(value)
        setattr(instance, self.storage_name, value)
```

## Complexity

Each access has expected O(1) instance-dictionary work plus validator cost. Storage is one reference per managed field per instance and one name per descriptor; this is not a bound on validator work. [^py313-descriptor] [^py313-model]

## Edge cases

Test two attributes on two instances, class access, unset access and rejected writes retaining the old value.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

def positive_int(value):
    if type(value) is not int:
        raise TypeError("expected int")
    if value <= 0:
        raise ValueError("expected positive value")
class Pair:
    left = Validated(positive_int)
    right = Validated(positive_int)
a, b = Pair(), Pair()
a.left, a.right, b.left, b.right = 1, 2, 3, 4
assert (a.left, a.right, b.left, b.right) == (1, 2, 3, 4)
assert Pair.left is vars(Pair)["left"]
with pytest.raises(ValueError):
    a.left = 0
assert a.left == 1 and a.right == 2 and b.left == 3
with pytest.raises(TypeError):
    a.right = True
assert a.right == 2
with pytest.raises(AttributeError):
    _ = Pair().left
```

## Evaluation guide

### Expected signals

Reject invalid values before mutation. Explain why storing a value on self shares it across owners.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would storage change for a class using only slots?

## Sources

<!-- generated from frontmatter -->
