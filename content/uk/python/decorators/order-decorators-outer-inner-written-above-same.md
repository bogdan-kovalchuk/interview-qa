---
id: py-decor-0002
title: "У якому порядку застосовуються два decorators `@outer` і `@inner`, записані над однією функцією?"
description: "Decorators застосовуються знизу вгору: спочатку @inner, потім @outer, тобто еквівалент func = outer(inner(func))."
track: python
section: decorators
level: middle
type: mechanism
tags: [outer, inner]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L3-L79
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Decorators застосовуються знизу вгору: спочатку `@inner`, потім `@outer`, тобто еквівалент `func = outer(inner(func))`.**[^py314-glossary-term-decorator] Кожний наступний decorator отримує результат попереднього.

```python
def outer(func):
    print('outer applied')
    return func

def inner(func):
    print('inner applied')
    return func

@outer
@inner
def hello(): pass
```

Вивід при визначенні: `inner applied`, потім `outer applied`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
