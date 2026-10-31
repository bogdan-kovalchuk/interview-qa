---
id: emb-periph-0018
title: "What UART, USART, I2C, and SPI characteristics matter when choosing a peripheral interface?"
track: embedded
section: peripherals-and-buses
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
  - source_id: nxp-um10204
    title: "NXP UM10204: I2C-bus specification and user manual"
    url: https://www.nxp.com/docs/en/user-guide/UM10204.pdf
---

## Short answer

**UART/USART** is a simple point-to-point async/sync serial, good for logs or simple links. **I2C** has an addressable multi-drop bus, but lower speed and sensitivity to pull-ups/capacitance. **SPI** is fast and electrically simple, but needs a chip select per slave and has no standard addressing/error handling.[^dou-embedded-interview]

## Detailed explanation

TODO
