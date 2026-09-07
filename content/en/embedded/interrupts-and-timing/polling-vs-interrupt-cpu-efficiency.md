---
id: emb-irq-0001
title: "What is the difference between polling and interrupts?"
description: "Polling wastes CPU cycles actively reading peripheral state, while an interrupt lets the peripheral signal an event and frees the CPU until it occurs."
track: embedded
section: interrupts-and-timing
level: junior
type: comparison
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

**Polling** – the CPU continuously reads peripheral state in a loop: `while(!(UART->SR & TXE));`.[^dou-embedded-interview] Simple to implement, but the CPU stays busy even without events, wasting power and time.

**Interrupt** – the peripheral signals the CPU only when an event occurs. The CPU runs the main code, and on an interrupt request it saves context and executes the ISR; efficient CPU use, low latency.

Choice: polling – for simple cases with predictable events; interrupt – when events are infrequent, asynchronous or low latency is required.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->
