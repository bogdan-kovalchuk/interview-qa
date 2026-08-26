---
id: py-objtypes-0015
title: "Коли `Decimal` доцільніший за `float` і яку проблему він не вирішує автоматично без правильної precision та rounding policy?"
description: "Decimal доцільний, коли потрібне точне десяткове представлення: фінансові розрахунки, грошові значення, збереження значущих нулів (1.30 + 1.20 = 2.50)."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [decimal, float]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L444-L497
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Decimal` доцільний, коли потрібне точне десяткове представлення: фінансові розрахунки, грошові значення, збереження значущих нулів (`1.30 + 1.20 = 2.50`).**[^py314-reference-datamodel] Він усуває помилки двійкового представлення (`Decimal('0.1') + Decimal('0.2') == Decimal('0.3')` – точно `True`), але не вирішує автоматично проблему round-off при недостатній precision: арифметичний контекст (`decimal.getcontext()`) має стандартну precision 28 знаків, і якщо результат перевищує цю точність, відбувається округлення відповідно до поточної rounding policy.

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
