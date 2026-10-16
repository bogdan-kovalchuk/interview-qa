---
id: emb-conn-0010
title: "Що таке Ethernet frame і які поля важливі при роботі з raw Ethernet, AVB або industrial Ethernet?"
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

**Ethernet frame** містить destination/source MAC, EtherType або length, payload і FCS; VLAN tag може додати priority/VID. Для raw Ethernet важливі MAC filtering, MTU, padding і EtherType. Для AVB/industrial Ethernet критичні timestamping, priority/QoS, deterministic latency і взаємодія MAC/PHY/driver.[^dou-embedded-interview]

## Detailed explanation

TODO
