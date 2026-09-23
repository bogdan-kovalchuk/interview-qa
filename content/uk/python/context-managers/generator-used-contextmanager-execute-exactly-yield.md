---
id: py-ctxmgr-0005
title: "Чому generator, використаний з `@contextmanager`, повинен виконати рівно один `yield`?"
description: "Протокол @contextmanager відображає один yield на одну пару enter/exit; нуль або більше yield ламає цей контракт."
track: python
section: context-managers
level: middle
type: pitfall
tags: [contextmanager]
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

**Протокол `@contextmanager` відображає один `yield` на одну пару enter/exit; нуль або більше yield ламає цей контракт.**[^py314-reference-datamodel-with-statement-context-managers] Якщо generator не виконує `yield` (наприклад, достроковий `return`), `@contextmanager` raise `RuntimeError: generator didn't yield`. Якщо виконує додатковий `yield` після першого – `RuntimeError: generator didn't stop`. Це гарантує, що enter і exit виконуються рівно один раз.

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
