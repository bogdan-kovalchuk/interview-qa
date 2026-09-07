---
id: emb-irq-0002
title: "What is a watchdog?"
description: "A Watchdog Timer resets the microcontroller if the program does not periodically feed it, protecting against hangs and infinite loops."
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

**Watchdog Timer (WDT)** is a hardware timer that automatically resets the microcontroller if the program does not "feed" it in time.[^dou-embedded-interview]

Principle: the program must regularly write a special value to the WDT register ("kick" or "feed"). If this does not happen, the timer fires and a system reset is performed.

Protects against: program hang, infinite loop, stack overflow. Types: **IWDG** (independent, runs from a separate oscillator, does not stop when the main clock stops) and **WWDG** (window watchdog – must be fed only within a specific time window, protects against feeding too early).

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
