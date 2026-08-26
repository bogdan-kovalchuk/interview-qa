---
id: py-prac-0020
title: "Реалізуйте validation descriptor, який зберігає значення окремо для кожного instance і працює з двома managed attributes."
description: "__set_name__ зберігає унікальний attr_name для кожного descriptor instance (наприклад, _val_name, _val_age), __get__/__set__ використовують getattr/setattr з цим attr_name для per-instance storage."
track: python
section: practical-coding
level: middle
type: coding
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: false
sources:
  - source_id: py314-tutorial
    title: "Python 3.14: Tutorial"
    url: https://docs.python.org/3.14/tutorial/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference
    title: "Python 3.14: Reference"
    url: https://docs.python.org/3.14/reference/
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L453-L511
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Task

TODO

## Constraints

TODO

## Short answer

**`__set_name__` зберігає унікальний `attr_name` для кожного descriptor instance (наприклад, `_val_name`, `_val_age`), `__get__`/`__set__` використовують `getattr`/`setattr` з цим `attr_name` для per-instance storage.** <span class="warn">Class-level access (`User.name`) повертає сам descriptor – це дозволяє introspection та декоратори.</span>

```python
class Validated:
    def __init__(self, validator):
        self.validator = validator
        self.attr_name = None

    def __set_name__(self, owner, name):
        self.attr_name = f'_val_{name}'

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self.attr_name, None)

    def __set__(self, instance, value):
        self.validator(value)
        setattr(instance, self.attr_name, value)
```

## Detailed explanation

TODO

## Examples

TODO

## Solution

TODO

## Complexity

TODO

## Edge cases

TODO

## Tests

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
