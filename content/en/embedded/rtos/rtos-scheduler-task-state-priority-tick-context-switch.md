---
id: emb-rtos-0012
title: "How does an RTOS scheduler work, and what do task state, priority, tick, and context switch mean?"
description: "An RTOS scheduler selects a ready task, while task state, priority, tick, and context switch describe scheduling and switching."
track: embedded
section: rtos
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for rtos concepts; details of specific devices and toolchains can differ."
---

## Short answer

An RTOS scheduler selects the ready task with the highest priority or by policy for equal priority. **Task state** describes ready, running, blocked, or suspended; **tick** provides the system time base; **context switch** saves the current task's registers and restores another. Preemption allows a higher-priority task to preempt a lower one.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
