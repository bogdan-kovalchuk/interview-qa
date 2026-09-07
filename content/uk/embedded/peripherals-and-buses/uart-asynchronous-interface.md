---
id: emb-periph-0008
title: "Що таке UART?"
description: "UART – асинхронний послідовний інтерфейс із TX/RX, узгодженим baud rate та кадром зі start, data, optional parity і stop bits."
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

**Universal Asynchronous Receiver-Transmitter** – асинхронний послідовний інтерфейс. Два дроти: `TX` (передача) і `RX` (прийом). Немає спільного тактового сигналу – обидва пристрої заздалегідь домовляються про **baud rate** (напр. 115200 бод).[^dou-embedded-interview]

Кадр: START bit -> data bits -> parity (опційно) -> STOP bit(s); Типово використовують 8 data bits, але hardware/configuration можуть підтримувати 5–9; UART описує framing даних; електричні рівні можуть бути TTL/CMOS, RS-232, RS-485 тощо.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
