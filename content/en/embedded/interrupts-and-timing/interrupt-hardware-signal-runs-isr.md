---
id: emb-irq-0003
title: "What is an interrupt?"
description: "An interrupt is a hardware or software signal that makes the CPU suspend its code and run an ISR, saving and later restoring context."
track: embedded
section: interrupts-and-timing
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
  - source_id: cmsis-core-nvic
    title: "CMSIS-Core (Cortex-M): Interrupts and Exceptions (NVIC)"
    url: https://arm-software.github.io/CMSIS_6/latest/Core/group__NVIC__gr.html
    accessed: 2026-09-06
    kind: official
    version: "6.2.0"
    applicability: "Authoritative section-level reference for interrupts and timing concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Interrupt** is a hardware or software signal that forces the CPU to suspend the current code and execute a special function – an **ISR (Interrupt Service Routine)**.[^dou-embedded-interview]

Sequence: an event occurs, then the interrupt controller (NVIC), then the CPU saves context (PC, registers), executes the ISR, restores context and returns to the main code.

ISR rules: keep it short and fast; do not use blocking functions; shared variables must be `volatile`; critical sections (disable/enable IRQ for atomic access) may be needed.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
