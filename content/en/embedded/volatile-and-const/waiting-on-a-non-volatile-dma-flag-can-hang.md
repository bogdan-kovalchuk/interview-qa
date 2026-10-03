---
id: emb-volconst-0059
title: "Trap: what is wrong with this way of waiting for DMA?"
description: "If dma_done is modified by an ISR or callback, an asynchronous synchronization method compatible with the toolchain is needed."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Question code

```c
uint8_t dma_done = 0;

while (!dma_done) { }
```

## Short answer

<span class="warn">If `dma_done` is modified by an ISR or callback, an ordinary non-volatile flag does not reliably expose the change.</span>

An embedded compiler may keep a non-volatile value in a register or move the read out of the loop. DMA does not change a C variable directly; an ISR/callback notifies the CPU of completion.

Defense: use a volatile flag or atomic/RTOS mechanism compatible with the compiler and MCU; for an RTOS, prefer a semaphore/event notification over busy-wait.[^iso-c-n1570]

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
