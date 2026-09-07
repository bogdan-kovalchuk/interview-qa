---
id: emb-volconst-0059
title: "Trap: what is wrong with this way of waiting for DMA?"
description: "If dmadone is modified by an ISR or a DMA callback, it is missing volatile."
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

## Question code

```c
uint8_t dma_done = 0;

while (!dma_done) { }
```

## Short answer

<span class="warn">If `dma_done` is modified by an ISR or a DMA callback, it is missing `volatile`.</span>

The compiler can read `dma_done` once and stay in the loop forever. DMA hardware does not change a C variable directly, but a callback/ISR changes it asynchronously with respect to the main loop.

Defense: `static volatile uint8_t dma_done;`. For an RTOS, prefer a semaphore/event notification over busy-wait.[^embeddedinterviewlab]

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
