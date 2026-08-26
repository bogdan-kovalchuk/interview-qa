---
id: py-itergen-0015
title: "Чому не варто покладатися на garbage collection generator для своєчасного звільнення external resource?"
description: "Час виклику close() через GC невизначений: CPython використовує reference counting, але за наявності reference cycles або в інших реалізаціях Python generator може бути finalized значно пізніше або взагалі не бути."
track: python
section: iterators-and-generators
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
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md#L512-L520
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Час виклику `close()` через GC невизначений: CPython використовує reference counting, але за наявності reference cycles або в інших реалізаціях Python generator може бути finalized значно пізніше або взагалі не бути.**[^py314-library-stdtypes-iterator-types] Навіть у CPython generator з циклічними посиланнями потрапляє до cyclic GC, який працює періодично, а не миттєво. Для детермінованого звільнення ресурсів слід використовувати `try/finally` або context manager, а не покладатися на фіналізацію.

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
