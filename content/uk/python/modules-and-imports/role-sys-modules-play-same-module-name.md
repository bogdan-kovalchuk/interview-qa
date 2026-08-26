---
id: py-modimp-0002
title: "Яку роль відіграє `sys.modules` під час повторного імпорту того самого module name?"
description: "sys.modules – це кеш, який зберігає вже завантажені module objects; повторний import того самого імені повертає кешований об'єкт без пошуку та виконання коду."
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [sys-modules]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md#L51-L79
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`sys.modules` – це кеш, який зберігає вже завантажені module objects; повторний `import` того самого імені повертає кешований об'єкт без пошуку та виконання коду.**[^py314-reference-import] Якщо `sys.modules[name]` містить module object, import негайно повертає його. Якщо значення дорівнює `None`, виникає `ModuleNotFoundError`. Видалення ключа з `sys.modules` змушує наступний імпорт шукати та виконувати модуль заново, створюючи новий module object.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
