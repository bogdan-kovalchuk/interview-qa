---
id: emb-conn-0005
title: "Як працює BLE з погляду embedded firmware: advertising interval, connection parameters, GATT і power budget?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

У BLE device рекламується з **advertising interval**, після connection працює з negotiated connection interval, latency і supervision timeout. **GATT** описує services/characteristics для даних і команд. Power budget сильно залежить від radio wakeups, payload size, connection parameters, sleep states і того, чи firmware вчасно повертає MCU у low power.[^dou-embedded-interview]

## Detailed explanation

TODO
