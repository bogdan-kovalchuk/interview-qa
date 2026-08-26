---
id: py-modimp-0005
title: "У якому порядку Python шукає module через import machinery та `sys.path`?"
description: "Python спочатку перевіряє sys.modules, потім перебирає sys.meta_path, а якщо спрацьовує path-based finder – послідовно обходить записи sys.path."
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [sys-path]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md#L22-L31
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Python спочатку перевіряє `sys.modules`, потім перебирає `sys.meta_path`, а якщо спрацьовує path-based finder – послідовно обходить записи `sys.path`.**[^py314-reference-import] У `sys.meta_path` за замовчуванням три meta path finders: для built-in модулів, frozen модулів і path-based імпорту. Path-based finder перебирає `sys.path`, який ініціалізується з директорії скрипта, змінної `PYTHONPATH` та стандартних шляхів встановлення. Результати пошуку path entry finder кешуються в `sys.path_importer_cache`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
