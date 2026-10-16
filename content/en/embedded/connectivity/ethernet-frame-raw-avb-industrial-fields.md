---
id: emb-conn-0010
title: "What is an Ethernet frame and which fields matter when working with raw Ethernet, AVB, or industrial Ethernet?"
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

An **Ethernet frame** contains destination/source MAC, EtherType or length, payload and FCS; a VLAN tag can add priority/VID. For raw Ethernet, MAC filtering, MTU, padding and EtherType matter. For AVB/industrial Ethernet, timestamping, priority/QoS, deterministic latency and MAC/PHY/driver interaction are critical.[^dou-embedded-interview]

## Detailed explanation

TODO
