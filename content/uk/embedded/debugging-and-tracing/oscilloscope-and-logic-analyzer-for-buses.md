---
id: emb-debug-0003
title: "Як використовувати осцилограф або logic analyzer для перевірки UART/SPI/I2C і timing issues?"
description: "Осцилографом перевірити рівні напруги, edges, ringing, rise/fall time, clock і reset/power timing. Logic analyzer декодує UART/SPI/I2C frames, показує…"
track: embedded
section: debugging-and-tracing
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 3
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
    applicability: "Авторитетне джерело рівня секції для понять розділу debugging-and-tracing; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Осцилографом перевірити рівні напруги, edges, ringing, rise/fall time, clock і reset/power timing. Logic analyzer декодує UART/SPI/I2C frames, показує baud/clock, ACK/NACK, CS timing і gaps між bytes. Найкраще міряти trigger-ом на problem event і одночасно дивитися firmware GPIO marker, щоб зв'язати code path із сигналом.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

