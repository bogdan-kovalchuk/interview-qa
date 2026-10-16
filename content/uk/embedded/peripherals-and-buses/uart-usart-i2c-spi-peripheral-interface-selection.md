---
id: emb-periph-0018
title: "Які особливості UART, USART, I2C і SPI важливі при виборі периферійного інтерфейсу?"
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

**UART/USART** простий point-to-point async/sync serial, добрий для logs або простих links. **I2C** має addressable multi-drop bus, але нижчу швидкість і чутливість до pull-ups/capacitance. **SPI** швидкий і простий electrically, але потребує chip select на slave і не має стандартного addressing/error handling.[^dou-embedded-interview]

## Detailed explanation

TODO
