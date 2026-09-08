---
id: py-pkgenv-0001
title: "У чому різниця між requirements.txt і pyproject.toml для управління залежностями Python-проєкту?"
description: "pyproject.toml містить стандартизовані метадані проєкту та build system; requirements.txt зазвичай задає для pip вхідні дані інсталяції середовища, тому ці файли можуть використовуватися разом."
track: python
section: packaging-and-environments
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: pep621
    title: "PEP 621: Storing project metadata in pyproject.toml"
    url: https://peps.python.org/pep-0621/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "PEP, що стандартизував pyproject.toml для метаданих проєкту."
  - source_id: packaging-guide
    title: "Python Packaging User Guide: Writing pyproject.toml"
    url: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Офіційна документація з пакування Python."
  - source_id: pip-requirements-format
    title: "pip documentation: Requirements File Format"
    url: https://pip.pypa.io/en/stable/reference/requirements-file-format/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Офіційна специфікація pip про синтаксис і призначення requirements files."
---

## Short answer

**`pyproject.toml` є стандартизованою конфігурацією: `[build-system]` обирає build backend, а `[project].dependencies` оголошує вимоги для інсталяції, які стають метаданими distribution.**[^pep621][^packaging-guide] Файл `requirements.txt` зазвичай є вхідними даними pip для інсталяції середовища та може містити pins, hashes, indexes, URLs, constraints й includes; ні назва файла, ні фіксація версій не є обов'язковими.[^pip-requirements-format] Тому ці файли доповнюють, а не замінюють один одного: `pyproject.toml` описує проєкт і підтримувані діапазони залежностей, а lock file або повністю pinned requirements потрібні для відтворюваного середовища.

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
