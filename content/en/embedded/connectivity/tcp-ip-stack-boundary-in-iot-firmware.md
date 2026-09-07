---
id: emb-conn-0001
title: "How is the TCP/IP stack used in an IoT device, and where is the boundary between firmware, the OS, and the network stack?"
description: "On a bare-metal MCU the TCP/IP stack is often a library like lwIP, while on Embedded Linux it runs in the kernel."
track: embedded
section: connectivity
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for connectivity concepts; details of specific devices and toolchains can differ."
---

## Short answer

On a bare-metal MCU the TCP/IP stack is often provided by a library like lwIP, and the firmware directly controls the Ethernet/Wi-Fi driver and sockets-like API. In Embedded Linux the kernel contains the network stack and drivers, and the application works through the socket API. The boundary is where a frame from the hardware driver becomes a packet for the stack, and then an application protocol like MQTT/HTTP runs on top of TCP/TLS.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

