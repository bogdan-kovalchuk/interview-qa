---
id: py-prac-0020
title: "Реалізуйте validation descriptor, який зберігає значення окремо для кожного instance і працює з двома managed attributes."
description: "Запишіть private attribute name у __set_name__ та зберігайте values на owner instance."
track: python
section: practical-coding
level: middle
type: coding
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
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

Реалізуйте `Validated(validator)` через descriptor protocol. Підтримайте два managed attributes і зберігайте їхні values окремо між instances.

## Constraints

- Використовуйте один descriptor object на managed attribute.
- Owners мають instance __dict__ і резервують private storage names.
- Validators піднімають exception для invalid input.
- Class access повертає descriptor; unset instance attribute викликає AttributeError.

## Short answer

**Запишіть private attribute name у `__set_name__` та зберігайте values на owner instance.** Перевіряйте перед assignment, щоб failed writes зберігали попереднє value. Для class-level access повертайте сам descriptor.

## Detailed explanation

Descriptor належить class, тому збереження current value на ньому поділяло б state. Окремі private names ізолюють два fields, а instance storage – objects. Резервування private names і заборона descriptor reuse – явні limits цього простого design. [^py313-descriptor] [^py313-model]

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

Кожен access має expected O(1) instance-dictionary work плюс validator cost. Пам’ять – один reference на managed field кожного instance й одне name на descriptor; це не обмеження роботи validator. [^py313-descriptor] [^py313-model]

## Edge cases

Перевірте два attributes на двох instances, class access, unset access та збереження old value після rejected writes.

## Tests

Виконайте після блока Solution із встановленим pytest.

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

Відхиляйте invalid values до mutation. Поясніть, чому value на self стає shared між owners.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як зміниться storage для class лише зі slots?

## Sources

<!-- generated from frontmatter -->
