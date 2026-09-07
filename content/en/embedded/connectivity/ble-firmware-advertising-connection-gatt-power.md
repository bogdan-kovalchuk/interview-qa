---
id: emb-conn-0005
title: "How does BLE work from the embedded firmware perspective: advertising interval, connection parameters, GATT, and power budget?"
description: "A BLE device advertises at a set interval, connects with negotiated parameters, uses GATT for services and characteristics, and its power budget depends on radio activity and sleep states."
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

In BLE, a device advertises with an **advertising interval**, and after connection operates with negotiated connection interval, latency and supervision timeout. **GATT** defines services/characteristics for data and commands. Power budget depends heavily on radio wakeups, payload size, connection parameters, sleep states, and whether the firmware promptly returns the MCU to low power.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
