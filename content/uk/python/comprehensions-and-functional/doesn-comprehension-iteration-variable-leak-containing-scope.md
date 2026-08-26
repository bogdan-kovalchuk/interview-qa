---
id: py-compfn-0003
title: "Чому iteration variable comprehension не витікає в containing scope, але target assignment expression у comprehension може зв’язуватися в containing scope?"
description: "Comprehension створює окрему неявну scope для iteration variable, але := (assignment expression) спеціально прив'язує свій target у containing scope, оминаючи цю ізоляцію."
track: python
section: comprehensions-and-functional
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Comprehension створює окрему неявну scope для iteration variable, але `:=` (assignment expression) спеціально прив'язує свій target у containing scope, оминаючи цю ізоляцію.**[^py314-howto-functional] Наприклад, після `[y := x for x in data]` ім'я `y` доступне поза comprehension, тоді як `x` – ні. <span class="warn">Якщо в containing scope є `nonlocal` або `global` декларація для цього імені, `:=` її поважає.</span>

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
