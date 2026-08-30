---
id: emb-periph-0011
title: "Коли краще UART, а коли SPI, якщо порівнювати wiring, speed, duplex, clocking і device selection?"
description: "UART простий: TX/RX/GND, asynchronous, добрий для console, modem, GPS і повільних point-to-point links."
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

UART простий: TX/RX/GND, asynchronous, добрий для console, modem, GPS і повільних point-to-point links. SPI швидший, synchronous, full-duplex, але потребує SCLK/MOSI/MISO і окремий CS на device або decoder. Якщо треба high-throughput sensor/display/flash на платі – часто SPI; якщо довший простий serial link без shared clock – UART.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

