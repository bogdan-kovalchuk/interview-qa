---
id: emb-conn-0009
title: "How does TCP work in the context of a constrained embedded device: handshake, retransmission, buffers, and keepalive?"
description: "TCP provides an ordered byte stream over a three-way handshake with ACK, retransmission and windowing; on embedded, RAM buffers, partial I/O and reconnect logic matter, and keepalive alone cannot replace an application-level heartbeat."
track: embedded
section: connectivity
level: senior
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

TCP starts with a **three-way handshake**, then guarantees an ordered byte stream via ACK, retransmission, windowing and congestion control. On embedded, RAM buffers, timeout/reconnect logic, partial writes/reads and backpressure from the network stack matter. <span class="warn">Keepalive does not replace an application-level heartbeat if you need to detect a hung peer quickly.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
