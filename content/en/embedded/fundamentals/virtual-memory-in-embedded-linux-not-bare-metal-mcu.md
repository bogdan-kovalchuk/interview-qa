---
id: emb-fund-0011
title: "Why is virtual memory used in Embedded Linux, and why is it usually absent on a bare-metal MCU?"
description: "Virtual memory gives each process its own address space, memory protection, lazy mapping, shared libraries, mmap, and copy-on-write."
track: embedded
section: fundamentals
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
  - source_id: zephyr-introduction
    title: "Zephyr Project documentation: Introduction"
    url: https://docs.zephyrproject.org/latest/introduction/index.html
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for fundamentals concepts; details of specific devices and toolchains can differ."
---

## Short answer

Virtual memory gives each process its own address space, memory protection, lazy mapping, shared libraries, `mmap`, and copy-on-write. A bare-metal MCU typically has little RAM/Flash, deterministic requirements, and often only an MPU or no memory protection at all. Therefore it works with physical addresses, a linker script, and direct MMIO.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
