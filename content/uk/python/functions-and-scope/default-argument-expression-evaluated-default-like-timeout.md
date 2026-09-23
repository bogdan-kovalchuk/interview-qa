---
id: py-funcs-0007
title: "Коли обчислюється вираз default argument і чому default на кшталт `timeout=get_timeout()` може не відображати подальші зміни конфігурації?"
description: "Default-вираз обчислюється один раз – у момент виконання інструкції def, а не при кожному виклику функції."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [timeout-get-timeout]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Default-вираз обчислюється один раз – у момент виконання інструкції `def`, а не при кожному виклику функції.**[^py314-reference-compound-stmts-function-definitions] Функція зберігає посилання на вже обчислений об'єкт. Якщо `get_timeout()` повертає, наприклад, `30` під час імпорту модуля, то всі подальші виклики без аргументу отримуватимуть `30`, навіть якщо конфігурація змінилася. Для динамічного значення потрібно обчислювати його в тілі функції.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
