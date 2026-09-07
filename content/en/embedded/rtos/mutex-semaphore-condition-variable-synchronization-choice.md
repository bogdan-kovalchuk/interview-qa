---
id: emb-rtos-0008
title: "Which synchronization mechanisms are used in POSIX/RTOS, and when should you choose a mutex, semaphore, or condition variable?"
description: "A mutex protects shared state with one owner in a critical section."
track: embedded
section: rtos
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
  - source_id: freertos-kernel-book
    title: "FreeRTOS Kernel Book and Reference Manual"
    url: https://www.freertos.org/Documentation/02-Kernel/07-Books-and-manual/01-RTOS_book
    accessed: 2026-09-06
    kind: official
    version: "latest"
    applicability: "Authoritative section-level reference for rtos concepts; details of specific devices and toolchains can differ."
---

## Short answer

`mutex` protects shared state with a single owner in a critical section. `semaphore` counts resources or signals an event between ISR/task in RTOS style, if the API allows it. `condition variable` wakes threads waiting on a predicate under a mutex; it does not store the event by itself.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
