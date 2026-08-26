---
id: py-objtypes-0005
title: "Чому `y = x` не копіює mutable object і як mutation через `y` стає видимою через `x`?"
description: "Присвоювання y = x копіює лише посилання на об'єкт, а не сам об'єкт; обидва імена вказують на той самий mutable об'єкт."
track: python
section: objects-and-types
level: middle
type: mechanism
tags: [y-x]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L48-L93
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Присвоювання `y = x` копіює лише посилання на об'єкт, а не сам об'єкт; обидва імена вказують на той самий mutable об'єкт.**[^py314-reference-datamodel] Будь-яка зміна стану об'єкта через одне ім'я (наприклад, `y.append(3)` для списку) одразу відображається через інше, бо `x` і `y` посилаються на одну й ту саму ділянку пам'яті. Для незалежної копії потрібні `copy.copy()` або `copy.deepcopy()`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
