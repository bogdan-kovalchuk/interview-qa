---
id: emb-fund-0026
title: "How to formulate networking interview questions that test embedded practice rather than theoretical OSI recitation?"
description: "Frame networking questions around real scenarios like IP loss, MQTT storms or stale DMA packets so candidates demonstrate diagnosis across firmware, driver, PHY/MAC and wire level."
track: embedded
section: fundamentals
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
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

Ask through a scenario: device not getting an IP, MQTT reconnect storming, TCP buffer overflow, Ethernet DMA seeing a stale packet or ARP cache expiring. The candidate should explain what they would check at the firmware, driver, PHY/MAC, network stack and wire level. **A good question** requires diagnosis, trade-offs and constraints of the MCU/Linux target, not a list of OSI layers.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
