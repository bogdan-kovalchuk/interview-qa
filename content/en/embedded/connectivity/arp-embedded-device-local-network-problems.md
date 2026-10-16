---
id: emb-conn-0008
title: "What is ARP and when does an embedded device actually encounter ARP problems in a local network?"
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

**ARP** maps an IPv4 address to a MAC address within a local Ethernet/Wi-Fi segment. An embedded device encounters ARP at the first connect to a gateway/peer, on IP conflict, stale ARP cache, link flap, or sleep/wake scenarios. Symptoms: ping fails within the LAN, the first packet is lost, and after an IP/MAC change a gratuitous ARP is needed.[^dou-embedded-interview]

## Detailed explanation

TODO
