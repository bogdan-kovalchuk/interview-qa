---
id: emb-build-0024
title: "Як побудувати build system для MCU-проекту з bootloader, application, tests і hardware variants?"
description: "Розбий build на окремі targets: bootloader, app, shared drivers, host tests, target tests і board configs.Кожен target має свій linker script, startup…"
track: embedded
section: toolchain-and-build
level: senior
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Розбий build на окремі targets: `bootloader`, `app`, shared drivers, host tests, target tests і board configs. Кожен target має свій linker script, startup file, compile definitions, memory layout і output artifacts. Hardware variants краще описувати через board files/config targets, а не умовні блоки у кожному source file.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
