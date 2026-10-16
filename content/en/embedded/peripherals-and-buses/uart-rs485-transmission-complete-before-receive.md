---
id: emb-periph-0017
title: "How do you determine when UART/RS485 transmission is complete before switching the bus driver to receive?"
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

Wait not only for an empty TX buffer but for **transmission complete**: the shift register must also be empty. In practice this is a flag like `TC`, an interrupt/DMA complete plus a UART TC check, or a timer guard time for the protocol. <span class="warn">`TXE` often means only that the data register is ready, not that the last bit has finished on the wire.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
