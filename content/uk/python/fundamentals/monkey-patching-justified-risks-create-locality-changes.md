---
id: py-fund-0010
title: "Коли monkey patching може бути виправданим і які ризики воно створює для локальності змін, тестів та оновлення залежностей?"
description: "Monkey patching виправданий переважно як короткоживуча, контрольована підміна в тесті або вузький compatibility workaround, коли dependency injection недоступний."
track: python
section: fundamentals
level: middle
type: practical
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L300-L331
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Monkey patching виправданий переважно як короткоживуча, контрольована підміна в тесті або вузький compatibility workaround, коли dependency injection недоступний.**[^py314-reference-executionmodel] Він приховує залежності, змінює shared state, може зробити тести order-dependent і зламатися після оновлення dependency. У тестах краще застосовувати scoped `unittest.mock.patch()` у правильному namespace, щоб підміна гарантовано скасовувалася.

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
