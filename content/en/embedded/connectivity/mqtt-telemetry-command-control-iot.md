---
id: emb-conn-0011
title: "What is MQTT and why is it often used for telemetry and command/control in IoT?"
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

**MQTT** is a lightweight publish/subscribe protocol over TCP where clients exchange messages through a broker. It is convenient for telemetry and command/control via topics, QoS levels, retained messages and last will. On embedded, account for TLS cost, reconnect behavior, offline queue and RAM limits for payload/buffers.[^dou-embedded-interview]

## Detailed explanation

TODO
