---
id: emb-memlink-0015
title: "Що робить linker і як він розміщує секції .text, .rodata, .data, .bss, stack і heap?"
description: "Linker розв'язує symbols і розміщує program sections у Flash та RAM відповідно до linker script."
track: embedded
section: memory-and-linker
level: middle
type: concept
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

**Linker** вирішує symbols/relocations, підтягує потрібні objects з libraries і розміщує sections у memory regions. Зазвичай `.text`/`.rodata` ідуть у Flash, `.data` має load image у Flash і runtime address у RAM, `.bss` zero-init у RAM. Stack/heap межі задаються linker script або startup code, і помилка тут дає hard fault або corruption.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
