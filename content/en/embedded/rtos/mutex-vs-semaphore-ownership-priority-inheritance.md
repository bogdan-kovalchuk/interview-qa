---
id: emb-rtos-0009
title: "How does a mutex differ from a semaphore in threads and RTOS tasks?"
description: "A mutex has ownership and often supports priority inheritance, while a semaphore is a counter of permits or events without ownership."
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

`mutex` has ownership: the task or thread that locked it must unlock it, and it often supports priority inheritance. `semaphore` is a counter of permits or events without such ownership, so it can be given and taken for resources or signaling. For shared data protection, choose mutex; for producer-consumer signaling or pool count, choose semaphore.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
