---
id: emb-conn-0012
title: "What sits between the network interface and the MCU: PHY, MAC, transceiver, controller, DMA, and driver stack?"
description: "A PHY/transceiver converts signals to a digital link, a MAC/controller builds frames and drives DMA descriptors, and the driver stack initializes hardware, manages buffers and cache coherency, and handles IRQs."
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

The physical medium is handled by a **PHY/transceiver**, which converts electrical/radio signals into digital link signals. A **MAC/controller** forms frames, filters, interrupts and often works with DMA descriptors in RAM. The driver stack initializes the hardware, manages buffers/cache coherency, handles IRQs and passes packets to the TCP/IP or fieldbus stack.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
