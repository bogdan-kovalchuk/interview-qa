---
id: emb-periph-0020
title: "Як обрати між CAN, RS485, Ethernet і BLE для embedded-пристрою з конкретними вимогами до distance, bandwidth і reliability?"
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

Вибір роблять від вимог: distance, data rate, determinism, topology, noise immunity, power, cost і certification. **CAN** добрий для robust multi-node control, **RS485** - для довгих industrial links, **Ethernet** - для bandwidth/IP integration, **BLE** - для low-power wireless/mobile access. Також враховуй existing ecosystem, diagnostics і firmware update path.[^dou-embedded-interview]

## Detailed explanation

TODO
