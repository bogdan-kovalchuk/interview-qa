---
id: py-ctxmgr-0009
title: "Як `__aexit__` має завершити cleanup після `CancelledError`, не поглинувши cancellation завдання?"
description: "__aexit__ має виконати cleanup і потім або не перехоплювати CancelledError, або повторно її підняти, щоб cancellation дійшла до завдання."
track: python
section: context-managers
level: senior
type: practical
tags: [aexit, cancellederror]
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
---

## Short answer

**`__aexit__` має виконати cleanup і потім або не перехоплювати `CancelledError`, або повторно її підняти, щоб cancellation дійшла до завдання.**[^py314-reference-datamodel-with-statement-context-managers] `CancelledError` успадковує від `BaseException`, тому звичайний `except Exception` її не зловить. <span class="warn">Якщо код навмисно подавляє `CancelledError`, він зобов'язаний викликати `Task.uncancel()`, інакше structured concurrency (TaskGroup, timeout) працюватиме некоректно.</span> Загальне правило: cleanup -> re-raise.

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
