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

**Spinlock** is a synchronization primitive where a thread that cannot acquire the lock **spins in a loop**, continuously checking availability, instead of going to sleep.[^dou-embedded-interview]

Advantage: low latency when the wait is very short. In kernel space, spinlocks are used where sleep is forbidden; depending on the lock type and context, they may disable preemption or IRQs. In user space, a spinlock is just a busy waiting primitive.

Rule: <span class="warn">you must not sleep while holding a spinlock</span>; if the critical section is long or the code may block, prefer a mutex.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
