---
id: emb-periph-0012
title: "What is the advantage of synchronous interfaces with a shared clock compared with asynchronous UART?"
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

On a synchronous bus such as SPI/I2C the master supplies the clock, so the receiver does not have to recover bit timing from the baud rate on its own. This simplifies sampling and allows higher speeds on short traces or a controlled board. UART is simpler in wiring, but more sensitive to baud mismatch, jitter and framing errors.[^dou-embedded-interview]

## Detailed explanation

TODO
