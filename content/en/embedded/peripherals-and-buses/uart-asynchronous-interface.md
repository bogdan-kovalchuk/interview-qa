---
id: emb-periph-0008
title: "What is UART?"
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

**Universal Asynchronous Receiver-Transmitter** – an asynchronous serial interface. Two wires: `TX` (transmit) and `RX` (receive). No shared clock – both devices agree on the **baud rate** in advance (e.g. 115200 baud).[^dou-embedded-interview]

Frame: START bit -> data bits -> parity (optional) -> STOP bit(s); Typically 8 data bits are used, though hardware/configuration may support 5–9; UART describes data framing; electrical levels can be TTL/CMOS, RS-232, RS-485, etc.

## Detailed explanation

TODO
