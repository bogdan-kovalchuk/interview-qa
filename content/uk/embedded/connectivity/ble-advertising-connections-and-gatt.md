---
id: emb-conn-0003
title: "Як працює BLE на рівні advertising, connection, GATT service і characteristic?"
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

BLE peripheral рекламує advertising packets з address, flags і optional service data, а central сканує й ініціює connection. Після connection data model зазвичай GATT: services групують characteristics, а characteristic має value і properties типу read/write/notify. Для low-power telemetry важливі connection interval, MTU, notification rate і sleep між events.[^dou-embedded-interview]

## Detailed explanation

TODO
