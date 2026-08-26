---
id: py-fund-0011
title: "Чому автоматичне завантаження plugin-класів через reflection може бути гіршим за явний registry, навіть якщо усуває ручну реєстрацію?"
description: "Автоматичне завантаження через reflection робить набір активних plugin-класів неявним, крихким до зміни імен і таким, що не має allowlist."
track: python
section: fundamentals
level: senior
type: comparison
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L394-L407
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Автоматичне завантаження через reflection робить набір активних plugin-класів неявним, крихким до зміни імен і таким, що не має allowlist.**[^py314-reference-executionmodel] Reflection-сканування (динамічний `import` модулів пакета, пошук підкласів через `__subclasses__()` або `getattr`) залежить від конвенцій іменування, порядку import і може підхопити непередбачені класи – test doubles, deprecated aliases або сторонні типи. Явний registry (словник чи список) дає контрольований allowlist, зменшує import-time side effects і легко тестується, бо активний набір класів видно в коді, а не ховається за runtime-скануванням.

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
