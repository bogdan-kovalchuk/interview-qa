---
id: py-modimp-0014
title: "Чим import package/module відрізняється від installable distribution project з build metadata?"
description: "Import package/module – це runtime-концепція: директорія з __init__.py або окремий .py-файл, який import system знаходить і завантажує."
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
---

## Short answer

**Import package/module – це runtime-концепція: директорія з `__init__.py` або окремий `.py`-файл, який import system знаходить і завантажує.**[^py314-reference-import] Distribution project – це packaging-концепція: source tree з `pyproject.toml`, який визначає build metadata (name, version, dependencies) і описує, як build backend створює installable archive (wheel/sdist). Одна distribution може містити кілька import packages; `pip install` працює з distribution, а не з import packages напряму.

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
