---
id: emb-dtypes-0105
title: "How does DRAM differ from SRAM and what are the implications for latency, refresh, controller, and startup?"
description: "SRAM is fast and needs no refresh but is expensive in area; DRAM is denser but needs a controller, refresh, and calibration, and may be unavailable at early boot."
track: embedded
section: data-types-and-memory-layout
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**SRAM** is fast, simple for an MCU, requires no refresh, but is expensive in area and usually smaller. **DRAM** is denser and larger, but requires a memory controller, refresh, calibration/training, and has more complex latency. At startup, DRAM may be unavailable until the controller is initialized, so early boot typically runs from internal SRAM.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
