---
id: emb-irq-0009
title: "How is data transferred between an ISR and a main loop or RTOS task without a race condition?"
description: "Data moves between ISR and main loop or task via volatile/atomic flags, ring buffers, critical sections, RTOS queues or task notification, with volatile alone insufficient."
track: embedded
section: interrupts-and-timing
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
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
    accessed: 2026-09-06
    kind: official
    version: "6.2.0"
    applicability: "Authoritative section-level reference for interrupts and timing concepts; details of specific devices and toolchains can differ."
---

## Short answer

Use **volatile/atomic flags**, lock-free ring buffers, critical sections, RTOS queues/semaphores or direct task notification. Shared multi-byte state is protected by interrupt disable, mutex in task context or atomic operations, depending on the platform. <span class="warn">`volatile` alone does not make an operation atomic and does not resolve a race condition.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
