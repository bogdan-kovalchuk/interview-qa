---
id: emb-conn-0004
title: "How does TCP differ from UDP for telemetry, control commands, and firmware updates?"
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

TCP provides an ordered reliable byte stream with retransmission and flow control, making it suitable for firmware updates or commands where integrity matters. UDP provides datagrams with no delivery or ordering guarantee, but lower overhead and latency, useful for frequent telemetry samples or real-time data. If UDP is used for a critical command or update, reliability, ordering and authentication must be built on top.[^dou-embedded-interview]

## Detailed explanation

TODO
