---
id: emb-conn-0009
title: "How does TCP work in the context of a constrained embedded device: handshake, retransmission, buffers, and keepalive?"
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

TCP starts with a **three-way handshake**, then guarantees an ordered byte stream via ACK, retransmission, windowing and congestion control. On embedded, RAM buffers, timeout/reconnect logic, partial writes/reads and backpressure from the network stack matter. <span class="warn">Keepalive does not replace an application-level heartbeat if you need to detect a hung peer quickly.</span>[^dou-embedded-interview]

## Detailed explanation

TODO
