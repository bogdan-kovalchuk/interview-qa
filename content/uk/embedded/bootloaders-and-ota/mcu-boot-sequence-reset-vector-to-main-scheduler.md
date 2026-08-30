---
id: emb-boot-0005
title: "Що відбувається під час boot sequence MCU від reset vector до main або scheduler start?"
description: "Після reset CPU бере SP і reset handler з vector table, startup code копіює .data, очищає .bss, викликає constructors і переходить у main, далі ініціалізуються HAL/drivers і запускається scheduler."
track: embedded
section: bootloaders-and-ota
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? bootloaders-and-ota; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Після reset CPU бере initial stack pointer і reset handler з vector table.<br>Startup code налаштовує low-level runtime: clock мінімально або пізніше, копіює <code>.data</code> з flash у RAM, очищає <code>.bss</code>, викликає constructors у C++ і переходить у <code>main</code>.<br>Далі firmware ініціалізує HAL/drivers, interrupts, RTOS objects і запускає scheduler.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
