---
id: emb-irq-0004
title: "How does an MCU timer use a counter, prescaler, auto-reload, compare, and interrupt events?"
description: "A timer divides its clock with a prescaler, counts ticks, and creates update or compare events for interrupts or DMA."
track: embedded
section: interrupts-and-timing
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
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
    accessed: 2026-09-06
    kind: official
    version: "6.2.0"
    applicability: "Authoritative section-level reference for interrupts and timing concepts; details of specific devices and toolchains can differ."
---

## Short answer

The timer clock is divided by the `prescaler`, after which the `counter` counts ticks. `auto-reload` sets the period for the overflow/update event, and `compare` generates an event when the counter matches a channel. An interrupt or DMA trigger occurs on update/compare/capture if the corresponding flags and NVIC are enabled.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
