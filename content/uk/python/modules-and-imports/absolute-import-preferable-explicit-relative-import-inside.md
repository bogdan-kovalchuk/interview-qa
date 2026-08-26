---
id: py-modimp-0006
title: "Коли absolute import доречніший за explicit relative import усередині package?"
description: "Absolute import (from package.module import name) доречніший, коли важлива читабельність, стійкість до рефакторингу та можливість запуску модуля як скрипта."
track: python
section: modules-and-imports
level: middle
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/modules_and_packages.md#L91-L95
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Absolute import (`from package.module import name`) доречніший, коли важлива читабельність, стійкість до рефакторингу та можливість запуску модуля як скрипта.**[^py314-reference-import] Absolute imports працюють незалежно від того, як модуль було запущено – імпортом чи `python -m`. Relative imports (`from .module import name`) компактніші всередині великого пакета, але крихкі: при переміщенні файлу в інший пакет усі крапки потрібно перераховувати, а запуск модуля як скрипта стає неможливим без `-m`.

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
