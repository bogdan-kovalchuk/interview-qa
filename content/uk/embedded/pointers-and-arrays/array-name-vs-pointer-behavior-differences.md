---
id: emb-ptrarr-0001
title: "У чому різниця між ім'ям масиву та вказівником у C, і коли вони поводяться по-різному?"
description: "Масив є об'єктом фіксованого розміру, а вказівник є окремим об'єктом, що зберігає адресу; вираз із масивом перетворюється на вказівник у більшості, але не в усіх контекстах."
track: embedded
section: pointers-and-arrays
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
  - source_id: c17-standard
    title: "ISO/IEC 9899:2018 (C17 Standard)"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2310.pdf
    accessed: 2026-09-08
    kind: official
    version: "C17"
    applicability: "Офіційний стандарт мови C."
---

## Short answer

**Масив є об'єктом із фіксованою кількістю елементів, тоді як вказівник є окремим об'єктом, що зберігає адресу.** У більшості виразів масив перетворюється на вказівник на перший елемент, але цього не відбувається, коли масив є операндом `sizeof` або унарного `&`.[^c17-standard] Тому `sizeof arr` вимірює весь масив, `sizeof ptr` вимірює вказівник, а `&arr` має тип вказівника на масив. Масив не можна присвоїти, а non-const вказівник можна; проте в оголошенні параметра функції `int a[]` коригується до `int *a`.

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
