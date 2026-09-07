---
id: emb-irq-0005
title: "How does interrupt handling work on Cortex-M with the NVIC, vector table, priorities, and return from an ISR?"
description: "The vector table contains the initial stack pointer and handler addresses; the NVIC enables IRQs, sets pending state, and selects the highest priority."
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

The vector table contains the initial SP and handler addresses; the NVIC enables an IRQ, sets the pending state and selects the highest priority. On ISR entry, Cortex-M automatically stacks part of the registers, switches to handler mode and can perform nested interrupts. Return from ISR uses a special `EXC_RETURN` to restore context; in an RTOS this is also the point for a context switch.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
