---
id: emb-periph-0009
title: "Як пристрої взаємодіють на I2C: address, start/stop, ACK/NACK, arbitration і clock stretching?"
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

I2C master формує `START`, передає 7/10-bit address плюс R/W bit, а receiver відповідає ACK або NACK. `STOP` завершує transaction; repeated START дозволяє змінити напрям без відпускання bus. Arbitration потрібен для multi-master, а clock stretching дозволяє slave утримати SCL low, якщо йому треба більше часу.[^dou-embedded-interview]

## Detailed explanation

TODO
