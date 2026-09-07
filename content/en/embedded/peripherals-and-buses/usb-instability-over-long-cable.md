---
id: emb-periph-0014
title: "A USB device is unstable over a 5–10 metre distance. Which USB, cable, power, and alternative-interface limits should you check?"
description: "Check the speed-specific cable length limit, signal integrity, VBUS drop, grounding, and consider alternatives such as active cables, extenders, or a different bus."
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

Check the specification length limit for the required USB speed, cable quality, shielding, hubs/repeaters, and VBUS drop under load. At 5–10 m, signal integrity problems, ground potential difference, and device power below the minimum often appear. Alternatives: powered hub/active cable, USB extender, RS-485/CAN/Ethernet, or move the MCU closer to the sensor.[^dou-embedded-interview]

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
