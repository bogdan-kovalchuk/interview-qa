---
id: emb-periph-0015
title: "How do you read 256 channels when the MCU has only 8 GPIOs, and what are the trade-offs of multiplexers, shift registers, and an external ADC?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
---

## Short answer

For digital inputs, cascade shift registers or GPIO expanders over SPI/I2C; for analog, use analog multiplexers or an external multi-channel ADC. A multiplexer saves pins but needs settling time and sequential sampling; a shift register is fast for digital but cannot read analog. An external ADC gives better accuracy and sampling isolation, but adds cost, bus bandwidth, and driver complexity.[^dou-embedded-interview]

## Detailed explanation

TODO
