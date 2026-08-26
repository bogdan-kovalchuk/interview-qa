---
id: py-itergen-0012
title: "Як `throw()` і `close()` впливають на control flow усередині suspended generator?"
description: "throw() піднімає задану exception, а close() – GeneratorExit, саме в тій точці yield, де generator був призупинений."
track: python
section: iterators-and-generators
level: senior
type: mechanism
tags: [throw, close]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/iterator_and_generator.md#L338-L429
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`throw()` піднімає задану exception, а `close()` – `GeneratorExit`, саме в тій точці `yield`, де generator був призупинений.**[^py314-library-stdtypes-iterator-types] Якщо generator перехоплює виняток у `try/except` навколо `yield`, виконання продовжується і може повернути наступне `yield`-значення. Якщо виняток не оброблено – він поширюється до caller. <span class="warn">Якщо generator yield-не значення після отримання `GeneratorExit`, CPython підніме `RuntimeError`.</span>

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
