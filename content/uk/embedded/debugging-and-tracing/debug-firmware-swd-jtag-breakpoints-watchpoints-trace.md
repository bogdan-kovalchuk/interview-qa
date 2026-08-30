---
id: emb-debug-0001
title: "Як налагоджувати firmware на реальному MCU через SWD/JTAG, breakpoints, watchpoints і trace?"
description: "Підключити probe через SWD/JTAG, завантажити ELF із symbols і перевірити reset/halt sequence."
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

Підключити probe через SWD/JTAG, завантажити ELF із symbols і перевірити reset/halt sequence. Breakpoints ставлять зупинки в code, watchpoints ловлять read/write конкретної адреси, а trace/SWO/ETM показує події без грубого printf. Для ISR/DMA bugs краще комбінувати debugger з logic analyzer і не зупиняти timing-sensitive code без потреби.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

