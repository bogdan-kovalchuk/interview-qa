---
id: py-prac-0002
title: "Що надрукує `events = []; enabled = False; enabled and events.append(\"run\"); print(events)` і чому side effect не відбувся?"
description: "Надрукує [] – метод append не викликається."
track: python
section: practical-coding
level: middle
type: mechanism
tags: [events-enabled-false-enabled-and-events-append-run-print-events]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
---

## Short answer

**Надрукує `[]` – метод `append` не викликається.**[^py314-tutorial] Оператор `and` у Python використовує short-circuit evaluation: якщо лівий операнд хибний (`False`), правий операнд не обчислюється взагалі. Оскільки `enabled` дорівнює `False`, вираз `events.append("run")` ніколи не виконується, і список залишається порожнім.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
