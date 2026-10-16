---
id: emb-conn-0005
title: "How does BLE work from the embedded firmware perspective: advertising interval, connection parameters, GATT, and power budget?"
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

In BLE, a device advertises with an **advertising interval**, and after connection operates with negotiated connection interval, latency and supervision timeout. **GATT** defines services/characteristics for data and commands. Power budget depends heavily on radio wakeups, payload size, connection parameters, sleep states, and whether the firmware promptly returns the MCU to low power.[^dou-embedded-interview]

## Detailed explanation

TODO
