---
id: py-decor-0004
title: "Чого `functools.wraps` не гарантує щодо фактичної call signature wrapper-функції?"
description: "functools.wraps копіює лише metadata-атрибути (__name__, __doc__, __qualname__, __annotations__, __type_params__) і встановлює __wrapped__, але не змінює реальні параметри wrapper-функції."
track: python
section: decorators
level: senior
type: mechanism
tags: [functools-wraps]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L247-L278
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`functools.wraps` копіює лише metadata-атрибути (`__name__`, `__doc__`, `__qualname__`, `__annotations__`, `__type_params__`) і встановлює `__wrapped__`, але не змінює реальні параметри wrapper-функції.**[^py314-glossary-term-decorator] Wrapper залишається функцією з `(*args, **kwargs)`. `inspect.signature()` за замовчуванням переходить за `__wrapped__` і показує оригінальну сигнатуру, але фактичний callable приймає будь-які аргументи – тому помилки невідповідності параметрів виникають лише всередині wrapper-а або в обгорнутій функції.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
