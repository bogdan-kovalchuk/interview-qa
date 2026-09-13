---
id: emb-rtos-0006
title: "What is a spinlock?"
description: "A spinlock is a synchronization primitive where the thread spins in a loop waiting for the lock instead of sleeping; you must not sleep while holding it."
track: embedded
section: rtos
level: junior
type: concept
tags: []
status: published
updated: 2026-09-13
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

**Spinlock** is a synchronization primitive where a thread that cannot acquire the lock **spins in a loop**, checking availability instead of sleeping.[^dou-embedded-interview]

Advantage: low latency when the wait is very short. In kernel space spinlocks are used where sleeping is forbidden and, depending on lock type and context, may disable preemption or IRQs; in user space a spinlock is just busy waiting.

Rule: <span class="warn">you must not sleep while holding a spinlock</span>; for a long critical section or code that may block, prefer a mutex.
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
