---
id: py-oop-0027
title: "Як parameters `eq`, `frozen` та `unsafe_hash` впливають на генерацію `__eq__` і `__hash__` для `@dataclass`?"
description: "eq=True (default) генерує __eq__; frozen=True з eq=True генерує __hash__; frozen=False з eq=True встановлює __hash__ = None (unhashable); eq=False залишає __hash__ від superclass; unsafe_hash=True примусово генерує..."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [eq, frozen, unsafe-hash, hash, dataclass]
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

**`eq=True` (default) генерує `__eq__`; `frozen=True` з `eq=True` генерує `__hash__`; `frozen=False` з `eq=True` встановлює `__hash__ = None` (unhashable); `eq=False` залишає `__hash__` від superclass; `unsafe_hash=True` примусово генерує `__hash__`.**[^py314-reference-datamodel] Крім того, `frozen=True` додає `__setattr__`/`__delattr__`, що викликають `FrozenInstanceError`, емулюючи immutable instances. А `unsafe_hash=True` використовується, коли клас логічно immutable, але може бути mutable.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
