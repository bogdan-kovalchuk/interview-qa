---
id: emb-fund-0025
title: "How to choose between MCU, DSP, FPGA, or an analog controller for a power control task?"
description: "MCU fits control logic and moderate loops, DSP handles fast numerical algorithms, FPGA gives parallel deterministic timing, and analog controllers suit simple or fail-safe regulation."
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

**MCU** suits control logic, communication and moderate loops; **DSP** – for fast numerical control algorithms. **FPGA** provides parallelism and deterministic sub-microsecond timing, but is more expensive to develop. An analog controller is appropriate when simple, very fast or fail-safe regulation is needed without firmware dependency.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
