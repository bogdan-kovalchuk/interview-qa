---
id: emb-periph-0004
title: "Як відбувається комунікація через UART?"
description: "UART передає кадр як START bit, data bits, опційний parity і STOP bit; приймач синхронізується по фронту START і семплує по baud rate."
track: embedded
section: peripherals-and-buses
level: junior
type: mechanism
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

Лінія у стані IDLE тримається HIGH.[^dou-embedded-interview] Передавач:

- Опускає лінію в LOW на 1 біт-час – це **START bit**
- Передає data bits, зазвичай 8, але можливі 5–9 залежно від hardware/configuration
- Опційно: біт парності
- Піднімає лінію в HIGH – це **STOP bit**

Приймач синхронізується по фронту START і семплює лінію в середині кожного біт-часу. Якщо baud rate різний, дані будуть спотворені. TX одного з'єднується з RX іншого, спільна GND обов'язкова.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
