---
id: py-modimp-0008
title: "Що означає partially initialized module під час circular import і чому не всі його names уже доступні?"
description: "Partially initialized module – це module object, який уже доданий у sys.modules, але його exec_module() ще не завершився, тому доступні лише ті names, що були визначені до точки циклічного імпорту."
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: []
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

**Partially initialized module – це module object, який уже доданий у `sys.modules`, але його `exec_module()` ще не завершився, тому доступні лише ті names, що були визначені до точки циклічного імпорту.**[^py314-reference-import] Import machinery вставляє модуль у `sys.modules` до виконання коду, щоб запобігти нескінченній рекурсії. Якщо модуль A імпортує B, а B знову імпортує A, другий імпорт A повертає об'єкт, у якому визначені лише інструкції, що виконалися до рядка `import B`. Звернення до ще не визначених names викликає `ImportError` або `AttributeError`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
