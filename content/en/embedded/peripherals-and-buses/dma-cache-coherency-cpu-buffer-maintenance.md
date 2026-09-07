---
id: emb-periph-0010
title: "What is DMA, and what problems can occur between DMA, the cache, and the CPU?"
description: "DMA transfers data between a peripheral and memory without the CPU copying every byte."
track: embedded
section: peripherals-and-buses
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
  - source_id: zephyr-peripherals
    title: "Zephyr Project documentation: Peripherals"
    url: https://docs.zephyrproject.org/latest/hardware/peripherals/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for peripherals and buses concepts; details of specific devices and toolchains can differ."
---

## Short answer

**DMA** transfers data between a peripheral and memory without the CPU copying every byte. The problem is that the CPU cache may hold stale or not-yet-written data while DMA sees RAM directly. Before TX a cache clean/flush is needed; after RX – invalidate; plus proper alignment, memory barriers and buffers in DMA-accessible memory.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
