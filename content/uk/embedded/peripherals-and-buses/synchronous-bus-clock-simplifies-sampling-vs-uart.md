---
id: emb-periph-0012
title: "У чому перевага синхронних інтерфейсів зі спільним clock порівняно з асинхронним UART?"
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

У synchronous bus типу SPI/I2C master дає clock, тому receiver не має сам точно відновлювати bit timing з baud rate. Це спрощує sampling і дозволяє вищі швидкості на коротких трасах або контрольованій платі. UART простіший по wires, але чутливіший до baud mismatch, jitter і framing errors.[^dou-embedded-interview]

## Detailed explanation

TODO
