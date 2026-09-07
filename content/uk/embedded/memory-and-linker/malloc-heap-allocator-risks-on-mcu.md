---
id: emb-memlink-0012
title: "Як працює malloc на рівні heap allocator і чому динамічна пам'ять ризикована на MCU?"
description: "Практичне питання про embedded-розробку та її обмеження."
track: embedded
section: memory-and-linker
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 2
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

`malloc` бере блок із heap, веде metadata й шукає вільний chunk достатнього розміру; `free` повертає блок allocator-у. На MCU heap малий, allocator може бути недетермінований за часом і створювати fragmentation. <span class="warn">У long-running firmware це ризик failure у runtime</span>, тому часто використовують static buffers, pools або arena allocator.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

