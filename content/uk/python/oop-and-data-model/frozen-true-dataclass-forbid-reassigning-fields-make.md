---
id: py-oop-0031
title: "Чому `frozen=True` у `@dataclass` забороняє reassignment полів, але не робить вкладений mutable object незмінним?"
description: "frozen=True генерує __setattr__ і __delattr__, які raise FrozenInstanceError при спробі переприв’язати поле, але не контролює стан об’єктів, на які ці поля посилаються."
track: python
section: oop-and-data-model
level: middle
type: pitfall
tags: [frozen-true, dataclass]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L586-L713
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`frozen=True` генерує `__setattr__` і `__delattr__`, які raise `FrozenInstanceError` при спробі переприв’язати поле, але не контролює стан об’єктів, на які ці поля посилаються.**[^py314-reference-datamodel] Коли ви пишете `obj.field = value`, викликається `__setattr__` frozen-класу й операція блокується. Однак `obj.mutable_list.append(1)` не викликає `__setattr__` на dataclass – це виклик методу вкладеного об’єкта, тому проходить без помилки. Документація прямо зазначає: «It is not possible to create truly immutable Python objects».

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    items: list[int]

c = Config([1, 2])
c.items = [3]        # FrozenInstanceError
c.items.append(3)    # OK - c.items == [1, 2, 3]
```

## Detailed explanation

TODO

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
