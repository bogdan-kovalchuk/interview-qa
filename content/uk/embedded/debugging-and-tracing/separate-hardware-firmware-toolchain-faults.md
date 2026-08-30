---
id: emb-debug-0002
title: "Як відрізнити hardware fault, firmware bug і toolchain/configuration issue під час debug на платі?"
description: "Спершу перевірити power, clocks, reset, boot pins і signal levels осцилографом або logic analyzer."
track: embedded
section: debugging-and-tracing
level: middle
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
  - source_id: gdb-manual
    title: "Debugging with GDB"
    url: https://sourceware.org/gdb/current/onlinedocs/gdb.pdf
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? debugging-and-tracing; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

Спершу перевірити power, clocks, reset, boot pins і signal levels осцилографом або logic analyzer. Потім мінімізувати firmware до known-good test: blink, UART, single peripheral, без RTOS/DMA. Якщо симптом залежить від optimization, linker script, startup або wrong flags, це схоже на toolchain/config; якщо повторюється при мінімальному коді й видно на сигналах – hardware/power issue.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

