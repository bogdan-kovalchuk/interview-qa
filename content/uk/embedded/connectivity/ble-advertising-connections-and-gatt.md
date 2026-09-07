---
id: emb-conn-0003
title: "Як працює BLE на рівні advertising, connection, GATT service і characteristic?"
description: "BLE peripheral рекламує advertising packets з address, flags і optional service data, а central сканує й ініціює connection. Після connection data mod…"
track: embedded
section: connectivity
level: middle
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

BLE peripheral рекламує advertising packets з address, flags і optional service data, а central сканує й ініціює connection. Після connection data model зазвичай GATT: services групують characteristics, а characteristic має value і properties типу read/write/notify. Для low-power telemetry важливі connection interval, MTU, notification rate і sleep між events.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

