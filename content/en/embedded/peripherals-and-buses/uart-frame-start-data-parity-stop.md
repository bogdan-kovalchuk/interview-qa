---
id: emb-periph-0004
title: "How does UART communication work?"
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

The line is held HIGH in the IDLE state.[^dou-embedded-interview] Transmitter:

- Pulls the line LOW for 1 bit-time – this is the **START bit**
- Sends data bits, usually 8, though 5–9 are possible depending on hardware/configuration
- Optional: parity bit
- Raises the line HIGH – this is the **STOP bit**

The receiver synchronizes on the START edge and samples the line in the middle of each bit-time. If the baud rates differ, the data will be corrupted. TX of one side connects to RX of the other; a shared GND is mandatory.

## Detailed explanation

TODO
