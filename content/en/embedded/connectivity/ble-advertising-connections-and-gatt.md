---
id: emb-conn-0003
title: "How does BLE work at the level of advertising, connections, GATT services, and characteristics?"
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

A BLE peripheral broadcasts advertising packets with an address, flags and optional service data, while a central scans and initiates a connection. After the connection the data model is usually GATT: services group characteristics, and a characteristic has a value and properties such as read/write/notify. For low-power telemetry the key parameters are connection interval, MTU, notification rate and sleep between events.[^dou-embedded-interview]

## Detailed explanation

TODO
