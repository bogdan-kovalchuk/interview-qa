---
id: py-modimp-0010
title: "Чим regular package з `__init__.py` відрізняється від namespace package?"
description: "Regular package містить файл __init__.py, який виконується при імпорті, і має єдиний __path__; namespace package не має __init__.py і може об'єднувати підмодулі з кількох каталогів."
track: python
section: modules-and-imports
level: middle
type: comparison
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md#L32-L50
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Regular package містить файл `__init__.py`, який виконується при імпорті, і має єдиний `__path__`; namespace package не має `__init__.py` і може об'єднувати підмодулі з кількох каталогів.**[^py314-reference-import] Regular package походить з одного каталогу, а його `__path__` вказує на цей каталог. Namespace package (PEP 420, Python 3.3+) складається з «порцій» – кількох каталогів з однаковим ім'ям пакета, – а його `__path__` є динамічним ітератором, який шукає підмодулі в усіх порціях. `ModuleSpec.origin` namespace package дорівнює `None`.

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
