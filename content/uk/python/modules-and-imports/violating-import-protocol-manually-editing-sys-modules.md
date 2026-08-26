---
id: py-modimp-0004
title: "Як порушення import protocol або ручне редагування `sys.modules` може призвести до двох module objects для одного source file?"
description: "Якщо завантажити той самий файл під різними qualified names (наприклад, через SourceFileLoader з різними іменами або додавши різні шляхи в sys.path), у sys.modules з'являться два окремі module objects для одного source..."
track: python
section: modules-and-imports
level: senior
type: pitfall
tags: [sys-modules]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md#L51-L79
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Якщо завантажити той самий файл під різними qualified names (наприклад, через `SourceFileLoader` з різними іменами або додавши різні шляхи в `sys.path`), у `sys.modules` з'являться два окремі module objects для одного source file.**[^py314-reference-import] <span class="warn">Це небезпечно, коли модуль зберігає стан (singleton, кеш, реєстр): копія-«двійник» матиме власну незалежну копію стану, і `isinstance`-перевірки класів з такого модуля можуть давати хибний результат.</span> Стандартний import protocol запобігає цьому, використовуючи fully qualified name як ключ у `sys.modules`.

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
