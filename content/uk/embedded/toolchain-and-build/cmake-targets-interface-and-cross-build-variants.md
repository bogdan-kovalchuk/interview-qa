---
id: emb-build-0021
title: "Як CMake може описувати залежності, targets, interface include dirs і cross-platform build variants?"
description: "У CMake кожна library/application має бути target з власними sources, compile definitions, include dirs і link dependencies.target_include_directories…"
track: embedded
section: toolchain-and-build
level: senior
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
  - source_id: gcc-overall-options
    title: "GCC manual: Options Controlling the Kind of Output"
    url: https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу toolchain-and-build; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

У CMake кожна library/application має бути **target** з власними sources, compile definitions, include dirs і link dependencies. `target_include_directories(... INTERFACE)` публікує headers для consumers, а `PRIVATE` лишає їх локальними. Cross-build variants задають toolchain file, presets, target-specific options і окремі targets для MCU, host tests та utilities.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
