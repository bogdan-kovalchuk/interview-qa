---
id: py-modimp-0011
title: "Які завдання доречно виконувати в package `__init__.py`, а які створюють небажані import-time side effects?"
description: "У __init__.py доречно розміщувати lightweight ініціалізацію пакета: експорт публічного API через __all__, convenience re-exports (from .sub import Class) та конфігурацію, яка не вимагає I/O."
track: python
section: modules-and-imports
level: middle
type: practical
tags: [init-py]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний посібник із packaging для Python."
---

## Short answer

**У `__init__.py` доречно розміщувати lightweight ініціалізацію пакета: експорт публічного API через `__all__`, convenience re-exports (`from .sub import Class`) та конфігурацію, яка не вимагає I/O.**[^py314-reference-import] Небажані import-time side effects – це heavy обчислення, мережеві виклики, запис у файли або зміна глобального стану: вони виконуються при кожному `import` пакета, уповільнюють запуск і створюють приховані залежності від порядку ініціалізації.

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
