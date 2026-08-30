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
---

## Short answer

**Serial Peripheral Interface** – синхронний послідовний інтерфейс.[^dou-embedded-interview] Чотири лінії: `SCK` (clock), `MOSI` (Master Out Slave In), `MISO` (Master In Slave Out), `CS/SS` (Chip Select, активний LOW).

Архітектура master-slave. Повний дуплекс. Висока швидкість (десятки MHz). Окремий CS для кожного slave. Немає адресації – вибір пристрою через CS. Немає ACK. Типово: Flash-пам'ять, АЦП, дисплеї, SD-карти.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
