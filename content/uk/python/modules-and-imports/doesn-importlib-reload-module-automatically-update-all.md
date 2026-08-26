---
id: py-modimp-0013
title: "Чому `importlib.reload(module)` не оновлює автоматично всі раніше створені instances та names, імпортовані через `from ... import ...`?"
description: "importlib.reload() перезапускає код модуля в тому самому module object, але не оновлює назв, скопійованих через from ... import ... в інші модулі, і не змінює класи вже створених instance'ів."
track: python
section: modules-and-imports
level: senior
type: pitfall
tags: [importlib-reload-module, from-import]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний посібник із packaging для Python."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md#L51-L79
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`importlib.reload()` перезапускає код модуля в тому самому module object, але не оновлює назв, скопійованих через `from ... import ...` в інші модулі, і не змінює класи вже створених instance'ів.**[^py314-reference-import] Причина: `from ... import ...` копіює посилання на об'єкт у namespace importing-модуля – reload не модифікує чужі namespace. Клас-об'єкт у reload-модулі стає новим, але існуючі instance'и продовжують посилатися на старий class object. Крім того, якщо нова версія модуля не визначає якесь ім'я, його стара дефініція залишається в module dict.

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
