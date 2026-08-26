---
id: py-syntax-0008
title: "Чому `continue` усередині `try` не скасовує виконання відповідного `finally` перед наступною ітерацією?"
description: "finally завжди виконується «на виході» з try, незалежно від того, чи вихід відбувається через return, break або continue."
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [continue]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`finally` завжди виконується «на виході» з `try`, незалежно від того, чи вихід відбувається через `return`, `break` або `continue`.**[^py314-reference-expressions] Коли `continue` виконується в `try`-блоці, Python спочатку виконує `finally`-клаузу, і лише потім переходить до наступної ітерації циклу. <span class="warn">Якщо `finally` сам виконує `return`, `break` або `continue`, це перезаписує збережену інструкцію з `try`.</span>

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
