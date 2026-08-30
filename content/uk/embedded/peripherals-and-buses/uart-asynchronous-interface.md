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

<span class="key">Universal Asynchronous Receiver-Transmitter</span> – асинхронний послідовний інтерфейс. Два дроти: <code>TX</code> (передача) і <code>RX</code> (прийом). Немає спільного тактового сигналу – обидва пристрої заздалегідь домовляються про <span class="key">baud rate</span> (напр. 115200 бод).[^dou-embedded-interview]

Кадр: START bit -> data bits -> parity (опційно) -> STOP bit(s). Типово використовують 8 data bits, але hardware/configuration можуть підтримувати 5–9. UART описує framing даних; електричні рівні можуть бути TTL/CMOS, RS-232, RS-485 тощо.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
