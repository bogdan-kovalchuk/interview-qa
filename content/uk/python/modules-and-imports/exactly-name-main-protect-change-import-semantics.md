---
id: py-modimp-0012
title: "Що саме захищає `if __name__ == \"__main__\"` і чого він не змінює в import semantics?"
description: "if __name__ == \"__main__\" захищає код від виконання під час імпорту: коли модуль запускають як скрипт, __name__ дорівнює \"__main__\", а при звичайному import – своїй dotted name."
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [if-name-main]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: null
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md#L15-L21
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`if __name__ == "__main__"` захищає код від виконання під час імпорту: коли модуль запускають як скрипт, `__name__` дорівнює `"__main__"`, а при звичайному import – своїй dotted name.**[^py314-reference-import] Цей guard не змінює import semantics: модуль все одно завантажується в `sys.modules`, а якщо той самий файл запустити як скрипт і потім імпортувати, CPython створить два різні module objects (`__main__` та import name) з окремими namespace.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
