---
id: py-objtypes-0022
title: "Чим parameterized static type на кшталт `list[str]` відрізняється від runtime-перевірки вмісту конкретного списку?"
description: "list[str] – це статична анотація типу, яку type checker (mypy, pyright) перевіряє під час аналізу коду; Python у runtime не валідує вміст контейнера."
track: python
section: objects-and-types
level: senior
type: comparison
tags: [list-str]
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
---

## Short answer

**`list[str]` – це статична анотація типу, яку type checker (mypy, pyright) перевіряє під час аналізу коду; Python у runtime не валідує вміст контейнера.**[^py314-reference-datamodel] Runtime-перевірка (наприклад `all(isinstance(x, str) for x in lst)`) виконується під час виконання програми й працює з реальними даними, а не з декларацією. У Python 3.14 parameterized generics на кшталт `list[str]` доступні як builtin subscription, але не вставляють жодних runtime-checkів у код.

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
