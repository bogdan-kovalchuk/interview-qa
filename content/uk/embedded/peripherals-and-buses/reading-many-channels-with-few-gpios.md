---
id: emb-periph-0015
title: "Як зчитати 256 каналів, якщо у MCU доступно тільки 8 GPIO, і які trade-offs мають multiplexers, shift registers та external ADC?"
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

Для digital inputs можна каскадувати shift registers або GPIO expanders по SPI/I2C; для analog – analog multiplexers або external multi-channel ADC. Multiplexer економить pins, але потребує settling time і sequential sampling; shift register швидкий для digital, але не читає analog. External ADC дає кращу точність/ізоляцію sampling, але додає cost, bus bandwidth і driver complexity.[^dou-embedded-interview]

## Detailed explanation

TODO
