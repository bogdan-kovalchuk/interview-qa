---
id: emb-boot-0006
title: "Які способи firmware update існують: wired flashing, bootloader, dual-bank, A/B image, OTA і rollback?"
description: "Wired flashing через SWD/JTAG/UART простий для factory/service, bootloader приймає image з UART/USB/CAN/network, dual-bank або A/B дозволяють записати новий image без стирання робочого, rollback повертає на попередню valid версію."
track: embedded
section: bootloaders-and-ota
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
  - source_id: mcuboot-design
    title: "MCUboot design documentation"
    url: https://docs.mcuboot.com/design.html
    accessed: 2026-09-06
    kind: official
    version: "current"
    applicability: "Авторитетне джерело рівня секції для понять розділу bootloaders-and-ota; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Wired flashing** через SWD/JTAG/UART простий для factory/service, але не для field updates. Bootloader може приймати image з UART/USB/CAN/network; dual-bank або A/B дозволяють записати новий image без стирання робочого. Rollback потрібен, щоб повернутися на попередню valid версію після failed boot або health check.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
