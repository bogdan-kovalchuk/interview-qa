---
id: emb-periph-0001
title: "Що таке `SPI`?"
description: "SPI – синхронний повнодуплексний послідовний інтерфейс master-slave на чотирьох лініях без адресації та ACK."
track: embedded
section: peripherals-and-buses
level: junior
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

**Serial Peripheral Interface** – синхронний послідовний інтерфейс. Чотири лінії: `SCK` (clock), `MOSI` (Master Out Slave In), `MISO` (Master In Slave Out), `CS/SS` (Chip Select, активний LOW).

Архітектура master-slave. Повний дуплекс. Висока швидкість (десятки MHz); Окремий CS для кожного slave; Немає адресації – вибір пристрою через CS; Немає ACK; Типово: Flash-пам'ять, АЦП, дисплеї, SD-карти.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
