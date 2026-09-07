---
id: emb-periph-0013
title: "An encoder produces many pulses and the MCU hangs at high speed. How do you assess interrupt rate, debounce, timer capture, and CPU load?"
description: "Calculate the edge rate from pulses per revolution, RPM and edges per pulse, then move to timer capture, DMA or a hardware counter when the ISR load is too high."
track: embedded
section: peripherals-and-buses
level: middle
type: pitfall
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

Calculate the edge rate: pulses per revolution × RPM × edges per pulse, and compare it with the ISR time. If an ISR on every edge takes a significant share of CPU, switch to timer encoder mode/input capture, DMA, or a hardware counter. <span class="warn">Debounce via ISR delays only makes things worse</span>; a mechanical encoder needs hardware/filter or a non-blocking state machine.[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
