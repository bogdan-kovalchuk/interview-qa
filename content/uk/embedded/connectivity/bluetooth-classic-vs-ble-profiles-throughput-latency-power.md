---
id: emb-conn-0006
title: "Чим Bluetooth Classic відрізняється від BLE за профілями, throughput, latency і power consumption?"
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

**Bluetooth Classic** орієнтований на постійніші з'єднання і профілі на кшталт audio/serial, часто з вищим throughput і більшим power cost. **BLE** оптимізований для коротких подій, advertising, GATT data model і низьке споживання. Для sensors/control BLE зазвичай кращий, для audio або legacy SPP частіше потрібен Classic.[^dou-embedded-interview]

## Detailed explanation

TODO
