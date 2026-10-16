---
id: emb-periph-0009
title: "How do devices communicate on I2C using addresses, start/stop, ACK/NACK, arbitration, and clock stretching?"
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

The I2C master issues `START`, sends a 7/10-bit address plus the R/W bit, and the receiver responds with ACK or NACK. `STOP` ends the transaction; a repeated START allows a direction change without releasing the bus. Arbitration is needed for multi-master, and clock stretching lets a slave hold SCL low when it needs more time.[^dou-embedded-interview]

## Detailed explanation

TODO
