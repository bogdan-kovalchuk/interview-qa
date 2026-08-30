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
  - source_id: gnu-ld-manual
    title: "GNU linker ld manual"
    url: https://sourceware.org/binutils/docs/ld/index.html
    accessed: 2026-09-06
    kind: official
    version: "2.47"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? memory-and-linker; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

<code>malloc(size)</code> виділяє блок пам'яті заданого розміру, але <span class="warn">не ініціалізує</span> його: там можуть бути старі байти. <code>calloc(n, size)</code> виділяє пам'ять під <code>n</code> елементів по <code>size</code> байтів і заповнює її нулями.<br><br>Ще одна практична різниця: якісна реалізація <code>calloc</code> може перевіряти overflow множення <code>n * size</code>, тоді як у ручному <code>malloc(n * size)</code> цю перевірку легко забути. Обидві функції повертають <code>NULL</code> при помилці й пам'ять треба звільняти через <code>free</code>.[^dou-embedded-interview]
## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
