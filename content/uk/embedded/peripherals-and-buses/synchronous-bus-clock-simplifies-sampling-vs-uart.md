---
id: emb-periph-0012
title: "У чому перевага синхронних інтерфейсів зі спільним clock порівняно з асинхронним UART?"
description: "У synchronous bus типу SPI/I2C master дає clock, тому receiver не має сам точно відновлювати bit timing з baud rate."
track: embedded
section: peripherals-and-buses
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "??????????? ??????? ????? ?????? ??? ?????? ???? peripherals-and-buses; ?????? ?????????? ????????? ?? ???????????? ?????? ????????????."
---

## Short answer

У synchronous bus типу SPI/I2C master дає clock, тому receiver не має сам точно відновлювати bit timing з baud rate. Це спрощує sampling і дозволяє вищі швидкості на коротких трасах або контрольованій платі. UART простіший по wires, але чутливіший до baud mismatch, jitter і framing errors.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

