---
id: emb-conn-0005
title: "Як працює BLE з погляду embedded firmware: advertising interval, connection parameters, GATT і power budget?"
description: "BLE device рекламується з advertising interval, після connection працює з negotiated parameters, GATT описує services/characteristics, а power budget залежить від radio wakeups, payload, connection parameters і sleep states."
track: embedded
section: connectivity
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? connectivity; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

У BLE device рекламується з <span class="key">advertising interval</span>, після connection працює з negotiated connection interval, latency і supervision timeout.<br><span class="key">GATT</span> описує services/characteristics для даних і команд.<br>Power budget сильно залежить від radio wakeups, payload size, connection parameters, sleep states і того, чи firmware вчасно повертає MCU у low power.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
