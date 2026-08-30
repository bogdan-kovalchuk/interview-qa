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

Розбий build на окремі targets: <code>bootloader</code>, <code>app</code>, shared drivers, host tests, target tests і board configs.<br>Кожен target має свій linker script, startup file, compile definitions, memory layout і output artifacts.<br>Hardware variants краще описувати через board files/config targets, а не умовні блоки у кожному source file.[^dou-embedded-interview]
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
