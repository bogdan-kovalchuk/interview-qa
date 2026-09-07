---
id: emb-periph-0018
title: "Які особливості UART, USART, I2C і SPI важливі при виборі периферійного інтерфейсу?"
description: "UART/USART - простий point-to-point serial для logs і простих links; I2C - addressable multi-drop bus з нижчою швидкістю; SPI - швидкий synchronous з chip select, без стандартного addressing."
track: embedded
section: peripherals-and-buses
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Авторитетне джерело рівня секції для понять розділу peripherals-and-buses; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
---

## Short answer

**UART/USART** простий point-to-point async/sync serial, добрий для logs або простих links. **I2C** має addressable multi-drop bus, але нижчу швидкість і чутливість до pull-ups/capacitance. **SPI** швидкий і простий electrically, але потребує chip select на slave і не має стандартного addressing/error handling.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
