---
id: emb-rtos-0013
title: "What is an RTOS task, and how does it differ from an interrupt handler and a bare-metal superloop?"
description: "An RTOS task has its own stack and priority, an interrupt handler runs in interrupt context, and a bare-metal superloop has no scheduler."
track: embedded
section: rtos
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for rtos concepts; details of specific devices and toolchains can differ."
---

## Short answer

**RTOS task** has its own stack, priority, and scheduler-managed state. An interrupt handler runs asynchronously in interrupt context, must be short, and does not behave like a regular task. A bare-metal superloop is a single main loop without a scheduler; concurrency there is typically built on flags, ISRs, and state machines.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
