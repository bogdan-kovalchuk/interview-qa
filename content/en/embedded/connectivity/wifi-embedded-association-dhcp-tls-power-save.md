---
id: emb-conn-0007
title: "How does Wi-Fi work on an embedded device and what are the implications of association, DHCP, TLS, and power save modes?"
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

Embedded Wi-Fi goes through scan/auth/association with an AP, then obtains an IP via DHCP or static config. TLS adds CPU/RAM cost, certificates, entropy and long handshakes, which matters for a small MCU. Power save modes reduce consumption but add latency, buffering at the AP, and more complex reconnect/error paths.[^dou-embedded-interview]

## Detailed explanation

TODO
