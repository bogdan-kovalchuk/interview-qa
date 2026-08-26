---
id: py-decor-0010
title: "Чому state у closure decorator може створити race condition при паралельних викликах обгорнутої функції?"
description: "Closure зберігає спільний mutable state в enclosing scope, і всі потоки, що викликають декоровану функцію, звертаються до однієї й тієї ж змінної без синхронізації."
track: python
section: decorators
level: senior
type: pitfall
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L80-L111
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Closure зберігає спільний mutable state в enclosing scope, і всі потоки, що викликають декоровану функцію, звертаються до однієї й тієї ж змінної без синхронізації.**[^py314-glossary-term-decorator] У CPython з GIL прості операції типу `x += 1` для integer атомарні на рівні bytecode, але складніші патерни (check-then-act, оновлення dict/list з умовами) не є атомарними навіть з GIL. У free-threaded CPython (3.13+) навіть прості операції не захищені GIL, тому closure-state потребує явного lock (наприклад, `threading.Lock`) або immutable state.

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
