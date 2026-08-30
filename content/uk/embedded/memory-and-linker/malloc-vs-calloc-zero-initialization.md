---
id: emb-memlink-0004
title: "Чим відрізняється malloc від calloc?"
description: "malloc виділяє пам'ять без ініціалізації і бере один аргумент, а calloc виділяє n*size байтів, обнуляє їх і перевіряє переповнення множення."
track: embedded
section: memory-and-linker
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-06
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
---

## Short answer

`malloc(size)` – виділяє `size` байтів, <span class="warn">не ініціалізує</span> їх.[^dou-embedded-interview] Один аргумент.

`calloc(n, size)` – виділяє `n * size` байтів і **ініціалізує їх нулями**. Два аргументи; хороша реалізація також перевіряє overflow множення `n * size`.

Приклад: `int *a = malloc(10 * sizeof(int));` – початкові значення невизначені; `int *b = calloc(10, sizeof(int));` – всі елементи = 0. Обидва повертають `NULL` при помилці.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
