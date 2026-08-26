---
id: py-decor-0005
title: "Чим decorator factory відрізняється від самого decorator і на якому етапі обробляються її arguments?"
description: "Decorator factory – це функція, що повертає decorator; її аргументи обчислюються один раз при decoration, а повернутий decorator потім застосовується до функції."
track: python
section: decorators
level: middle
type: comparison
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L130-L190
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Decorator factory – це функція, що повертає decorator; її аргументи обчислюються один раз при decoration, а повернутий decorator потім застосовується до функції.**[^py314-glossary-term-decorator] Наприклад, `@has_perm('view')` спочатку викликає `has_perm('view')` (factory), яка повертає справжній decorator, і вже він отримує декоровану функцію. Без factory синтаксис `@decorator(arg)` неможливий, бо decorator приймає лише один аргумент – callable.

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
