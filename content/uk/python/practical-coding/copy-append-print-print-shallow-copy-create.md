---
id: py-prac-0003
title: "Що надрукує `a = [[1]]; b = a.copy(); b[0].append(2); print(a)` і як shallow copy створює цей aliasing bug?"
description: "Надрукує [[1, 2]] – a теж бачить зміну."
track: python
section: practical-coding
level: middle
type: pitfall
tags: [a-1-b-a-copy-b-0-append-2-print-a]
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

**Надрукує `[[1, 2]]` – `a` теж бачить зміну.**[^py314-tutorial] Метод `list.copy()` створює shallow copy: новий зовнішній список, але вкладені об'єкти копіюються лише за посиланням. Тому `b[0]` і `a[0]` – це той самий об'єкт `list`, і `append(2)` через `b` мутує його спільно. <span class="warn">Для глибокого копіювання потрібний `copy.deepcopy()`.</span>

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
