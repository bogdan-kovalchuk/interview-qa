---
id: emb-conn-0006
title: "How does Bluetooth Classic differ from BLE in profiles, throughput, latency, and power consumption?"
description: "Bluetooth Classic suits persistent audio/serial links with higher throughput and power; BLE targets short events, advertising, GATT and low consumption, so BLE fits sensors while Classic fits audio and legacy SPP."
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

**Bluetooth Classic** targets more persistent connections and profiles like audio/serial, often with higher throughput and greater power cost. **BLE** is optimized for short events, advertising, GATT data model and low consumption. For sensors/control BLE is usually better; for audio or legacy SPP, Classic is more often needed.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
