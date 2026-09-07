---
id: emb-fund-0015
title: "Що таке socket у Linux і коли embedded-пристрій реально потребує socket API?"
description: "<span class=\"key\">Socket</span> – file descriptor для endpoint-у network або local IPC."
track: embedded
section: fundamentals
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
    applicability: "Авторитетне джерело рівня секції для понять розділу fundamentals; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**Socket** – file descriptor для endpoint-у network або local IPC. Embedded-пристрій потребує socket API, коли говорить TCP/UDP, Unix domain IPC, Bluetooth sockets або має daemon/client архітектуру. Для простого sensor-to-MCU без OS socket не потрібен; там буде UART/SPI/I2C або lightweight network stack API.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

