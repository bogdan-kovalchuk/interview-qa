---
id: emb-fund-0023
title: "How should you approach writing a simple Linux kernel driver for a character device or platform device?"
description: "A character device defines file operations, while a platform driver implements probe and remove, handles devicetree resources, MMIO, and IRQs."
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

For a character device, define file operations: `open`, `read`, `write`, `ioctl`, plus registration and lifetime cleanup. For a platform driver, implement `probe`/`remove`, take resources from devicetree, map MMIO, register IRQ, and expose the interface. <span class="warn">In a kernel driver you cannot think like in user space: different allocation rules, locking, sleep context, and error handling.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
