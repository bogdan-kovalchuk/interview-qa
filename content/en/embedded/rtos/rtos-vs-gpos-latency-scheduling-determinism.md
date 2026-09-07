---
id: emb-rtos-0010
title: "What is an RTOS, and how does it differ from a general-purpose OS in latency, scheduling, and determinism?"
description: "An RTOS provides bounded interrupt and task latency, priority-based scheduling, and primitives for deterministic embedded tasks."
track: embedded
section: rtos
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for rtos concepts; details of specific devices and toolchains can differ."
---

## Short answer

**RTOS** provides bounded interrupt and task latency, priority-based scheduling, and primitives for deterministic embedded tasks. A general-purpose OS optimises throughput, fairness, and multi-user capabilities, so latency can be less predictable. An RTOS does not guarantee "fast always"; it provides controlled worst-case conditions when code and priorities are designed correctly.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
