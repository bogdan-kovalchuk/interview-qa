---
id: emb-fund-0026
title: "How to formulate networking interview questions that test embedded practice rather than theoretical OSI recitation?"
track: embedded
section: fundamentals
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
---

## Short answer

Ask through a scenario: device not getting an IP, MQTT reconnect storming, TCP buffer overflow, Ethernet DMA seeing a stale packet or ARP cache expiring. The candidate should explain what they would check at the firmware, driver, PHY/MAC, network stack and wire level. **A good question** requires diagnosis, trade-offs and constraints of the MCU/Linux target, not a list of OSI layers.[^dou-embedded-interview]

## Detailed explanation

TODO
