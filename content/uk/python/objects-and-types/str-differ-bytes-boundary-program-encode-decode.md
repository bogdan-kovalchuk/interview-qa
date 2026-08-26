---
id: py-objtypes-0017
title: "Чим `str` відрізняється від `bytes` і на якій межі програми має відбуватися encode/decode?"
description: "str – незмінна послідовність Unicode code point (текст), bytes – незмінна послідовність 8-бітних значень (двійкові дані); вони не сумісні напряму і потребують явного encode/decode."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [str, bytes]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L498-L586
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`str` – незмінна послідовність Unicode code point (текст), `bytes` – незмінна послідовність 8-бітних значень (двійкові дані); вони не сумісні напряму і потребують явного encode/decode.**[^py314-reference-datamodel] Encode/decode має відбуватися на межі програми: decode при читанні зовнішніх даних (файли, мережа, CLI) у внутрішній `str`, encode при записі `str` назовні. <span class="warn">Змішування `str` і `bytes` в операціях викликає `TypeError`, а неявне кодування всередині програми призводить до помилок при зміні encoding.</span>

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
