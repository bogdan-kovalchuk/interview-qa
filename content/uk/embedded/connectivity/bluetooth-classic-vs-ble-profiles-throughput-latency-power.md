---
id: emb-conn-0006
title: "Чим Bluetooth Classic відрізняється від BLE за профілями, throughput, latency і power consumption?"
description: "Bluetooth Classic орієнтований на постійніші з'єднання і профілі audio/serial з вищим throughput і power cost; BLE оптимізований для коротких подій, advertising, GATT і низьке споживання."
track: embedded
section: connectivity
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу connectivity; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Bluetooth Classic** орієнтований на постійніші з'єднання і профілі на кшталт audio/serial, часто з вищим throughput і більшим power cost. **BLE** оптимізований для коротких подій, advertising, GATT data model і низьке споживання. Для sensors/control BLE зазвичай кращий, для audio або legacy SPP частіше потрібен Classic.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
