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

**Memory barrier** is an instruction or compiler primitive that constrains reordering of memory operations by the compiler or CPU. It is needed when the order of accesses matters: lock-free code, MMIO regions, DMA, multi-core synchronization.[^dou-embedded-interview]

**Cache coherence** is consistency of data copies in caches of different CPUs/cores or between cache and memory accessed by DMA. If DMA wrote a buffer into RAM, the CPU may still see an old copy in cache without invalidate/clean.

In practice: atomics/barriers are used for shared memory, and cache clean/invalidate or non-cacheable buffers for DMA, depending on the MCU/MPU.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
