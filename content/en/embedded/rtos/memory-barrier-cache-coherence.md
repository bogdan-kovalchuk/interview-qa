---
id: emb-rtos-0007
title: "What are a memory barrier and cache coherence?"
description: "A memory barrier constrains memory operation reordering, while cache coherence keeps data copies consistent between CPUs, caches, and DMA."
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

**Memory barrier** is an instruction or compiler primitive that constrains reordering of memory operations by the compiler or CPU; it is needed where access order matters: lock-free code, MMIO, DMA, multi-core synchronization.[^dou-embedded-interview]

**Cache coherence** is consistency between cache copies in different cores, or between cache and memory touched by DMA: after DMA writes a buffer to RAM, the CPU may still see a stale cached copy without invalidate/clean.

In practice: atomics and barriers for shared memory, cache clean/invalidate or non-cacheable buffers for DMA, depending on the MCU/MPU.
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
