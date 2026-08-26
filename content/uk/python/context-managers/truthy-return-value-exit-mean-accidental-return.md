---
id: py-ctxmgr-0002
title: "Що означає truthy return value з `__exit__` і чому випадкове `return True` небезпечне?"
description: "Truthy return з __exit__ пригнічує exception – вона не поширюється далі за межі with."
track: python
section: context-managers
level: middle
type: pitfall
tags: [exit, return-true]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/namespace_and_context_manager.md#L3-L98
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Truthy return з `__exit__` пригнічує exception – вона не поширюється далі за межі `with`.**[^py314-reference-datamodel-with-statement-context-managers] <span class="warn">Випадкове `return True` ковтає будь-який exception, включно з `TypeError`, `KeyboardInterrupt` та помилками в самому cleanup-коді.</span> Це ускладнює діагностику: баг у тілі `with` стає невидимим. Зазвичай безпечніше повертати `False` або `None` і подавлювати лише очікувані типи через явну перевірку.

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
