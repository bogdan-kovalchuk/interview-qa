---
id: py-ctxmgr-0010
title: "Чим reusable context manager відрізняється від reentrant context manager?"
description: "Reusable можна використовувати в кількох окремих with blocks, але не можна вкладати всередину самого себе; reentrant можна і повторно використовувати, і вкладати рекурсивно."
track: python
section: context-managers
level: middle
type: comparison
tags: []
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

**Reusable можна використовувати в кількох окремих `with` blocks, але не можна вкладати всередину самого себе; reentrant можна і повторно використовувати, і вкладати рекурсивно.**[^py314-reference-datamodel-with-statement-context-managers] Приклад reusable: `contextlib.ExitStack`, `threading.Lock` – новий `with` працює, але вкладений `with` на тому ж instance зламає стан. Приклад reentrant: `threading.RLock`, `contextlib.redirect_stdout` – вони коректно обробляють вкладеність, зберігаючи попередній стан у внутрішньому стеку.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
