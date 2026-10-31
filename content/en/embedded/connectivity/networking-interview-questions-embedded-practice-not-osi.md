---
id: emb-fund-0026
title: "How to formulate networking interview questions that test embedded practice rather than theoretical OSI recitation?"
track: embedded
section: connectivity
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
  - source_id: rfc-2131-dhcp
    title: "RFC 2131: Dynamic Host Configuration Protocol"
    url: https://www.rfc-editor.org/rfc/rfc2131
  - source_id: rfc-5227-ipv4-acd
    title: "RFC 5227: IPv4 Address Conflict Detection"
    url: https://www.rfc-editor.org/rfc/rfc5227
  - source_id: rfc-9293-tcp
    title: "RFC 9293: Transmission Control Protocol (TCP)"
    url: https://www.rfc-editor.org/rfc/rfc9293
  - source_id: oasis-mqtt-v5
    title: "OASIS: MQTT Version 5.0"
    url: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
---

## Short answer

Ask through a scenario: device not getting an IP, MQTT reconnect storming, TCP buffer overflow, Ethernet DMA seeing a stale packet or ARP cache expiring. The candidate should explain what they would check at the firmware, driver, PHY/MAC, network stack and wire level. **A good question** requires diagnosis, trade-offs and constraints of the MCU/Linux target, not a list of OSI layers.[^dou-embedded-interview]

## Detailed explanation

TODO
