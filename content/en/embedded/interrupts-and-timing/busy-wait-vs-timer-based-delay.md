---
id: emb-irq-0007
title: "How is delay implemented in firmware, and why is busy-wait often worse than a timer-based approach?"
description: "Delay can be implemented as a busy loop, cycle counter, SysTick, hardware timer or RTOS sleep, with timer-based approaches preferred over busy-wait."
track: embedded
section: interrupts-and-timing
level: senior
type: pitfall
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

Delay can be a busy loop, CPU cycle counter, SysTick, hardware timer or RTOS sleep. **Timer-based delay** better preserves CPU time, allows sleep/power saving and does not break when the clock or optimization changes. <span class="warn">Busy-wait blocks the main loop/task and scales poorly for ISR-driven or RTOS firmware.</span>[^dou-embedded-interview]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
