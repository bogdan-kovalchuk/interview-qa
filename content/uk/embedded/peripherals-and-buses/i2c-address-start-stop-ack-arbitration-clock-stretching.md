---
id: emb-periph-0009
title: "Як пристрої взаємодіють на I2C: address, start/stop, ACK/NACK, arbitration і clock stretching?"
description: "I2C master формує <code>START</code>, передає 7/10-bit address плюс R/W bit, а receiver відповідає ACK або NACK."
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

I2C master формує <code>START</code>, передає 7/10-bit address плюс R/W bit, а receiver відповідає ACK або NACK. <code>STOP</code> завершує transaction; repeated START дозволяє змінити напрям без відпускання bus. Arbitration потрібен для multi-master, а clock stretching дозволяє slave утримати SCL low, якщо йому треба більше часу.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

