---
id: py-objtypes-0010
title: "Чому `copy.deepcopy()` використовує memo і як це допомагає з shared references або cyclic structures?"
description: "Memo – це словник {id(оригінал): копія}, який запобігає нескінченній рекурсії для циклічних посилань і уникає дублювання спільних об'єктів."
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [copy-deepcopy]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L442-L558
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Memo – це словник `{id(оригінал): копія}`, який запобігає нескінченній рекурсії для циклічних посилань і уникає дублювання спільних об'єктів.**[^py314-reference-datamodel] Коли `deepcopy` зустрічає об'єкт, який вже скопійовано (є в memo), він повертає існуючу копію замість рекурсивного копіювання. Для циклічної структури `a = []; a.append(a)` це єдиний спосіб завершити копіювання без `RecursionError`, зберігаючи структуру спільних посилань у копії.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
