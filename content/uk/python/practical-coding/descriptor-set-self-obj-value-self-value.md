---
id: py-prac-0011
title: "У descriptor з `__set__(self, obj, value): self._value = value` два instances бачать останнє записане value: чому так сталося і де зберігати per-instance state?"
description: "self у descriptor – це сам descriptor-об'єкт (один на клас), тому self._value є спільним для всіх instances класу-власника."
track: python
section: practical-coding
level: middle
type: pitfall
tags: [set-self-obj-value-self-value-value]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
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

## Short answer

**`self` у descriptor – це сам descriptor-об'єкт (один на клас), тому `self._value` є спільним для всіх instances класу-власника.**[^py314-tutorial] Descriptor створюється один раз як class attribute, і `__set__` викликається з різними `obj`, але `self._value` перезаписується щоразу. <span class="warn">Per-instance state треба зберігати на `obj`:</span> наприклад, через `obj.__dict__[self.name] = value` або через `WeakKeyDictionary`, ключований за `obj`, щоб уникнути витоків пам'яті.

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
