---
id: emb-periph-0008
title: "Що таке UART?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

**Universal Asynchronous Receiver-Transmitter** – асинхронний послідовний інтерфейс. Два дроти: `TX` (передача) і `RX` (прийом). Немає спільного тактового сигналу – обидва пристрої заздалегідь домовляються про **baud rate** (напр. 115200 бод).[^dou-embedded-interview]

Кадр: START bit -> data bits -> parity (опційно) -> STOP bit(s); Типово використовують 8 data bits, але hardware/configuration можуть підтримувати 5–9; UART описує framing даних; електричні рівні можуть бути TTL/CMOS, RS-232, RS-485 тощо.

## Detailed explanation

TODO
