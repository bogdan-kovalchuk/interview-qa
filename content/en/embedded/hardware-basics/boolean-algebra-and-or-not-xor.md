---
id: emb-hwbasic-0001
title: "What is Boolean algebra?"
description: "Boolean algebra is a mathematical system for true/false values with AND, OR, NOT and XOR operations, underlying logic gates in electronics and conditions in code."
track: embedded
section: hardware-basics
level: junior
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
    applicability: "Authoritative section-level reference for hardware basics concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Boolean algebra** is a mathematical system for true/false or 1/0 values.[^dou-embedded-interview] Basic operations: AND (`&&` or logical multiplication), OR (`||` or logical addition), NOT (`!`), and XOR.

In electronics it describes logic gates and digital circuits; in programming – conditions, masks, flags and optimization of logical expressions. For example, De Morgan's laws: `!(A && B) == (!A || !B)` and `!(A || B) == (!A && !B)`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
