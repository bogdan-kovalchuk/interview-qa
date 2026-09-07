---
id: emb-testemb-0002
title: "How should embedded C code be tested on the host and target, and what should each level cover?"
description: "Host tests cover portable logic, target tests cover hardware-dependent behavior and real timing."
track: embedded
section: testing-embedded
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
  - source_id: zephyr-testing
    title: "Zephyr Project documentation: Testing"
    url: https://docs.zephyrproject.org/latest/develop/test/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for testing embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Host tests** cover pure logic: state machines, parsers, protocol framing, boundary cases, mocks for HAL/MMIO. **Target tests** verify what depends on the hardware: clocks, drivers, DMA, ISR latency, buses, power states, and real timing. HIL or board tests must catch integration defects that unit tests on a PC cannot see.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

