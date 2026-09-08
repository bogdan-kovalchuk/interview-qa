---
id: py-typing-0001
title: "У чому різниця між List[str] з typing і list[str] вбудованим у Python 3.9+?"
description: "typing.List[str] є legacy typing alias; list[str] є вбудованим generic-синтаксисом із Python 3.9 і рекомендований, якщо цільова версія Python не старіша за 3.9."
track: python
section: typing-and-annotations
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
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pep585
    title: "PEP 585: Type Hinting Generics In Standard Collections"
    url: https://peps.python.org/pep-0585/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "PEP, що ввів вбудований generic-синтаксис."
---

## Short answer

**`typing.List[str]` є legacy typing alias, а `list[str]` є вбудованим generic-синтаксисом, запровадженим у Python 3.9 і рекомендованим для коду з цільовою версією 3.9 або новішою.**[^py314-library-typing][^pep585] Static type checkers зазвичай трактують обидва варіанти як список рядків. Проте це не ідентичні runtime objects, і жодна з цих анотацій не перевіряє елементи списку під час виконання. Python 3.8 не може обчислити `list[str]`; там використовуйте `typing.List[str]` або postpone annotation evaluation, якщо це підтримує решта tooling.

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
