---
id: emb-periph-0020
title: "How to choose between CAN, RS485, Ethernet, and BLE for an embedded device with specific distance, bandwidth, and reliability requirements?"
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

Choose from the requirements: distance, data rate, determinism, topology, noise immunity, power, cost, and certification. **CAN** is good for robust multi-node control, **RS485** – for long industrial links, **Ethernet** – for bandwidth/IP integration, **BLE** – for low-power wireless/mobile access. Also consider the existing ecosystem, diagnostics, and firmware update path.[^dou-embedded-interview]

## Detailed explanation

TODO
