---
id: emb-volconst-0052
title: "What does `volatile` mean in multi-threaded C/C++: is it a replacement for a mutex or an atomic?"
description: "No, volatile does not replace a mutex, an atomic, or RTOS synchronization."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">No. `volatile` does not replace a mutex, an atomic, or RTOS synchronization.</span>

It describes observable memory access, but provides no inter-thread synchronization, memory ordering, or race-free increments. In an embedded RTOS, tasks that share variables need atomic primitives, a mutex, a queue, a semaphore, or a critical section.

Rule: `volatile` for hardware/ISR/DMA visibility; synchronization primitives for concurrency correctness.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
