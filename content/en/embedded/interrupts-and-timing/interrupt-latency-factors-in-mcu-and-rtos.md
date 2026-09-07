---
id: emb-irq-0006
title: "What is interrupt latency, and what factors increase it in an MCU or RTOS?"
description: "Interrupt latency is the time from a hardware event to the first useful ISR instruction."
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

Interrupt latency is the time from a hardware event to the first useful instruction of the ISR. It is increased by disabled interrupts, higher-priority ISRs, long critical sections, flash wait states, cache misses, bus contention, FPU stacking and RTOS interrupt masking. To reduce latency, keep the ISR short and move heavy work to a task or deferred handler.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
