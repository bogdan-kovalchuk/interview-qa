---
id: emb-irq-0012
title: "What is an interrupt vector, and how does it differ between MCU startup code and the Linux kernel?"
description: "An MCU interrupt vector table contains handler addresses, while Linux hides interrupt routing behind its architecture and IRQ subsystems."
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

On an MCU the **interrupt vector table** usually sits at a fixed address and holds the initial stack pointer and handler addresses. The startup code provides weak default handlers, and the firmware replaces the ISR entries it needs. In Linux, hardware interrupt routing is hidden behind the architecture/kernel IRQ subsystem: a driver registers its handler through the kernel API rather than editing the startup vector table directly.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
