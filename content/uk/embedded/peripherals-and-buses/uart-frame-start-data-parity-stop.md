---
id: emb-periph-0004
title: "Як відбувається комунікація через UART?"
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

Лінія у стані IDLE тримається HIGH.[^dou-embedded-interview] Передавач:

- Опускає лінію в LOW на 1 біт-час – це **START bit**
- Передає data bits, зазвичай 8, але можливі 5–9 залежно від hardware/configuration
- Опційно: біт парності
- Піднімає лінію в HIGH – це **STOP bit**

Приймач синхронізується по фронту START і семплює лінію в середині кожного біт-часу. Якщо baud rate різний, дані будуть спотворені. TX одного з'єднується з RX іншого, спільна GND обов'язкова.

## Detailed explanation

TODO
