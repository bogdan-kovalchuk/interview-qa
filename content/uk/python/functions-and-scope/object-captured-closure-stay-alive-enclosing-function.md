---
id: py-funcs-0019
title: "Чому об’єкт, захоплений closure, може залишатися живим після завершення зовнішньої функції, і як це впливає на утримання пам’яті?"
description: "Closure зберігає посилання на захоплені змінні через атрибут __closure__ (кортеж cell-об'єктів), тому ці об'єкти залишаються досяжними й не збираються GC, доки існує сама closure."
track: python
section: functions-and-scope
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
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Closure зберігає посилання на захоплені змінні через атрибут `__closure__` (кортеж cell-об'єктів), тому ці об'єкти залишаються досяжними й не збираються GC, доки існує сама closure.**[^py314-reference-datamodel] Це може призвести до неочікуваного утримання великих об'єктів у пам'яті: якщо closure захопила посилання на великий список і зберігається довго (наприклад, у callback), список теж залишається живим. Рішення – явно звільнити посилання (`del`) або не захоплювати зайві об'єкти.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
