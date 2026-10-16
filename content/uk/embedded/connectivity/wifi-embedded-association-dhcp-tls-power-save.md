---
id: emb-conn-0007
title: "Як працює Wi-Fi на embedded-пристрої і які наслідки мають association, DHCP, TLS і power save modes?"
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

Embedded Wi-Fi проходить scan/auth/association з AP, потім отримує IP через DHCP або static config. TLS додає CPU/RAM cost, certificates, entropy і довгі handshakes, що важливо для small MCU. Power save modes зменшують споживання, але додають latency, buffering у AP і складніші reconnect/error paths.[^dou-embedded-interview]

## Detailed explanation

TODO
