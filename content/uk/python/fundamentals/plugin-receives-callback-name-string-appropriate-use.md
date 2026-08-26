---
id: py-fund-0008
title: "Плагін отримує name callback як string: коли доречно використати `getattr(plugin, name)`, а коли безпечнішим API буде явний registry allowed callbacks?"
description: "getattr() доречний, коли dynamic attribute lookup є частиною довіреного контракту plugin API, а name уже перевірено."
track: python
section: fundamentals
level: middle
type: comparison
tags: [getattr-plugin-name]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L332-L393
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`getattr()` доречний, коли dynamic attribute lookup є частиною довіреного контракту plugin API, а name уже перевірено.**[^py314-reference-executionmodel] Якщо name надходить із конфігурації або зовнішнього вводу, явний registry краще фіксує allowlist, aliases і стабільний public API. Після `getattr()` все одно потрібно перевірити, що значення дозволене та callable.

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
