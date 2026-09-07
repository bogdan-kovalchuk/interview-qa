---
id: emb-memlink-0011
title: "Яка різниця між `calloc` і `malloc`?"
description: "`malloc` виділяє неініціалізовану пам'ять, тоді як `calloc` виділяє масив елементів і заповнює пам'ять нулями."
track: embedded
section: memory-and-linker
level: junior
type: comparison
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "Авторитетне джерело рівня секції для понять розділу memory-and-linker; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

`malloc(size)` виділяє блок пам'яті заданого розміру, але <span class="warn">не ініціалізує</span> його: там можуть бути старі байти. `calloc(n, size)` виділяє пам'ять під `n` елементів по `size` байтів і заповнює її нулями.

Ще одна практична різниця: якісна реалізація `calloc` може перевіряти overflow множення `n * size`, тоді як у ручному `malloc(n * size)` цю перевірку легко забути. Обидві функції повертають `NULL` при помилці й пам'ять треба звільняти через `free`.[^dou-embedded-interview]

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
