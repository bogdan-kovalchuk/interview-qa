---
id: py-objtypes-0014
title: "Чому `0.1 + 0.2 == 0.3` може бути `False` і як коректно порівнювати приблизні floating-point результати?"
description: "0.1 + 0.2 == 0.3 дає False, тому що float у Python зберігається як IEEE 754 binary64, і десяткові дроби 0.1 та 0.2 не мають точного двійкового представлення."
track: python
section: objects-and-types
level: middle
type: pitfall
tags: [0-1-0-2-0-3]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L401-L443
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`0.1 + 0.2 == 0.3` дає `False`, тому що `float` у Python зберігається як IEEE 754 binary64, і десяткові дроби 0.1 та 0.2 не мають точного двійкового представлення.**[^py314-reference-datamodel] Результат `0.1 + 0.2` дорівнює `0.30000000000000004`. Для коректного порівняння використовують `math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)`, який перевіряє `abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`. <span class="warn">При порівнянні з нулем обов'язково вказуйте `abs_tol > 0`, інакше `rel_tol` не дасть результату.</span>

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
