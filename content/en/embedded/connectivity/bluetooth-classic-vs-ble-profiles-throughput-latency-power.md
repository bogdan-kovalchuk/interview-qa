---
id: emb-conn-0006
title: "How does Bluetooth Classic differ from BLE in profiles, throughput, latency, and power consumption?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

**Bluetooth Classic** targets more persistent connections and profiles like audio/serial, often with higher throughput and greater power cost. **BLE** is optimized for short events, advertising, GATT data model and low consumption. For sensors/control BLE is usually better; for audio or legacy SPP, Classic is more often needed.[^dou-embedded-interview]

## Detailed explanation

TODO
