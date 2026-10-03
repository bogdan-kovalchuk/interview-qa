---
id: emb-volconst-0006
title: "What changes once `volatile` is added?"
description: "volatile preserves access semantics for rx_done, but does not provide atomicity or DMA coherency."
track: embedded
section: volatile-and-const
level: junior
type: mechanism
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
volatile uint8_t rx_done = 0;

while (rx_done == 0) { }
```

## Short answer

Each evaluation of volatile `rx_done` is an access under the abstract-machine rules; the C implementation defines what counts as such an access.[^iso-c-n1570]

This can let the main loop observe ISR changes in a supported toolchain; DMA also needs platform-specific memory and cache coordination. Without `volatile`, the compiler may reuse a value because the loop does not write `rx_done`.[^iso-c-n1570]

For a simple `uint8_t` flag, it may suffice for separate accesses on a particular implementation, but `volatile` does not ensure atomicity or safe read-modify-write operations.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
