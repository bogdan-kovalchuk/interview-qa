---
id: emb-periph-0001
title: "What is `SPI`?"
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

**Serial Peripheral Interface** – a synchronous serial interface. Four lines: `SCK` (clock), `MOSI` (Master Out Slave In), `MISO` (Master In Slave Out), `CS/SS` (Chip Select, active LOW).

Master-slave architecture. Full duplex. High speed (tens of MHz); Separate CS for each slave; No addressing – device selection via CS; No ACK; Typical: Flash memory, ADCs, displays, SD cards.[^dou-embedded-interview]

## Detailed explanation

TODO
