---
id: emb-periph-0020
title: "Як обрати між CAN, RS485, Ethernet і BLE для embedded-пристрою з конкретними вимогами до distance, bandwidth і reliability?"
description: "Вибір роблять від вимог: distance, data rate, determinism, topology, noise immunity, power, cost і certification. CAN добрий для robust multi-node control, RS485 для довгих industrial links, Ethernet для bandwidth/IP, BLE для low-power wireless."
track: embedded
section: peripherals-and-buses
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

Вибір роблять від вимог: distance, data rate, determinism, topology, noise immunity, power, cost і certification. **CAN** добрий для robust multi-node control, **RS485** - для довгих industrial links, **Ethernet** - для bandwidth/IP integration, **BLE** - для low-power wireless/mobile access. Також враховуй existing ecosystem, diagnostics і firmware update path.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
