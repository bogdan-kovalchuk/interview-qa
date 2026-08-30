---
id: emb-periph-0015
title: "Як зчитати 256 каналів, якщо у MCU доступно тільки 8 GPIO, і які trade-offs мають multiplexers, shift registers та external ADC?"
description: "Для digital inputs можна каскадувати shift registers або GPIO expanders по SPI/I2C; для analog – analog multiplexers або external multi-channel ADC. M…"
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
---

## Short answer

Для digital inputs можна каскадувати shift registers або GPIO expanders по SPI/I2C; для analog – analog multiplexers або external multi-channel ADC. Multiplexer економить pins, але потребує settling time і sequential sampling; shift register швидкий для digital, але не читає analog. External ADC дає кращу точність/ізоляцію sampling, але додає cost, bus bandwidth і driver complexity.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

