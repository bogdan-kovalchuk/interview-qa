---
id: emb-rtos-0001
title: "What is a race condition?"
description: "A race condition is a situation where the outcome depends on the execution order of threads, processes, or ISRs."
track: embedded
section: rtos
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for rtos concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Race condition** is a situation where the outcome depends on the execution order of threads, processes, or ISRs.[^dou-embedded-interview] If the order changes, the program may sometimes work correctly and sometimes produce an error.

Classic example: `counter++` is not a single atomic action but a sequence of read, modify, write; if two threads read the old value simultaneously, one increment can be lost.

Protection: `mutex`, spinlock, atomic operations, critical section, or briefly disabling interrupts in embedded code.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
