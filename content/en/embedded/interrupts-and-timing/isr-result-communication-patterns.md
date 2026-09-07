---
id: emb-irq-0010
title: "Why should an ISR not return a result like an ordinary function, and which patterns replace that?"
description: "An ISR is invoked by hardware, not a caller, so results are passed through flags, buffers, queues or task notification instead of a return value."
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

An ISR is invoked by a hardware/CPU exception mechanism, not by a caller expecting a return value. Results are passed through flags, buffers, queues, semaphores, event bits or deferred work/task notification. **An ISR should signal an event**, while heavy processing belongs in the main loop, a worker task or a bottom half.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
