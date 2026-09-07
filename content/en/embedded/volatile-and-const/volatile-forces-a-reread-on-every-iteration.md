---
id: emb-volconst-0006
title: "What changes once `volatile` is added?"
description: "The compiler must re-read rxdone from memory on every iteration, letting the main loop see changes made by the ISR or DMA."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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
volatile uint8_t rx_done = 0;

while (rx_done == 0) { }
```

## Short answer

The compiler must re-read `rx_done` from memory on every iteration.

This allows the main loop to see the change made by the ISR or DMA completion callback. Without `volatile`, the optimiser may decide the value is stable because there is no write to `rx_done` in the loop body.

Embedded rule: for a simple ISR flag of type `uint8_t`, `volatile` is often sufficient for visibility, but not for more complex read-modify-write scenarios.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
