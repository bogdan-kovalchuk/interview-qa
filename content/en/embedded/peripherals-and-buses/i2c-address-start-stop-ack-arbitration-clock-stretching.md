---
id: emb-periph-0009
title: "How do devices interact on I2C: address, start/stop, ACK/NACK, arbitration, and clock stretching?"
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

An I2C master asserts `START`, transmits a 7/10-bit address plus R/W bit, and the receiver answers with ACK or NACK. `STOP` ends the transaction; repeated START lets the master switch direction without releasing the bus. Arbitration enables multi-master operation, and clock stretching lets a slave hold SCL low when it needs more processing time.[^dou-embedded-interview]

## Detailed explanation

TODO
