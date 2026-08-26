---
id: py-modimp-0003
title: "Чому два `import module` зазвичай не виконують top-level code модуля двічі, але можуть створити різні local bindings?"
description: "Top-level code виконується лише при першому імпорті; усі наступні import повертають той самий module object з sys.modules, але кожен import-statement створює власні local bindings у просторі імен імпортера."
track: python
section: modules-and-imports
level: middle
type: comparison
tags: [import-module]
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

**Top-level code виконується лише при першому імпорті; усі наступні `import` повертають той самий module object з `sys.modules`, але кожен import-statement створює власні local bindings у просторі імен імпортера.**[^py314-reference-import] Наприклад, `import math` зв'язує локальне ім'я `math` з module object, а `from math import pi` зв'язує локальне `pi` безпосередньо з об'єктом `pi`. Обидва варіанти посилаються на той самий module object, але local names у модулі-імпортері різні.

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
