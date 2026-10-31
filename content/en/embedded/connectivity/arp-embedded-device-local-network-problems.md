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
  - source_id: rfc-826-arp
    title: "RFC 826: An Ethernet Address Resolution Protocol"
    url: https://www.rfc-editor.org/rfc/rfc826.html
  - source_id: rfc-1122-host-requirements
    title: "RFC 1122: Requirements for Internet Hosts – Communication Layers"
    url: https://www.rfc-editor.org/rfc/rfc1122.html
  - source_id: lwip-opts-arp
    title: "lwIP 2.1.0: ARP options (lwipopts.h)"
    url: https://www.nongnu.org/lwip/2_1_x/group__lwip__opts__arp.html
  - source_id: linux-man-arp
    title: "arp(7) – Linux manual page"
    url: https://man7.org/linux/man-pages/man7/arp.7.html
  - source_id: rfc-5227-ipv4-acd
    title: "RFC 5227: IPv4 Address Conflict Detection"
    url: https://www.rfc-editor.org/rfc/rfc5227.html
  - source_id: esp-idf-kconfig-lwip
    title: "ESP-IDF Programming Guide: Project Configuration (LWIP options)"
    url: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/kconfig-reference.html
  - source_id: rfc-2131-dhcp
    title: "RFC 2131: Dynamic Host Configuration Protocol"
    url: https://www.rfc-editor.org/rfc/rfc2131.html
---

## Short answer

**ARP** maps an IPv4 address to a MAC address within a local Ethernet/Wi-Fi segment. An embedded device encounters ARP at the first connect to a gateway/peer, on IP conflict, stale ARP cache, link flap, or sleep/wake scenarios. Symptoms: ping fails within the LAN, the first packet is lost, and after an IP/MAC change a gratuitous ARP is needed.[^dou-embedded-interview]

## Detailed explanation

TODO
