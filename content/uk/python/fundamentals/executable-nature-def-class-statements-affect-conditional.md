---
id: py-fund-0012
title: "Як executable nature інструкцій `def` і `class` впливає на умовне визначення, повторне визначення та import-time side effects?"
description: "def і class – виконувані інструкції (executable statements): вони створюють об'єкт функції або класу та прив'язують ім'я під час виконання, а не на етапі компіляції."
track: python
section: fundamentals
level: senior
type: mechanism
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
---

## Short answer

**`def` і `class` – виконувані інструкції (executable statements): вони створюють об'єкт функції або класу та прив'язують ім'я під час виконання, а не на етапі компіляції.**[^py314-reference-executionmodel] Тому їх можна розміщувати всередині `if`/`else`, циклів і вкладених scope – визначиться лише та гілка, яка справді виконається. Повторний `def` або `class` з тим самим ім'ям у тій самій області просто переприв'язує ім'я до нового об'єкта. Оскільки тіло модуля виконується згору вниз при import, будь-який код на рівні модуля (I/O, мережеві виклики, print) стає import-time side effect, що ускладнює тестування та повторне використання.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
