---
id: emb-align-0030
title: "What does `__attribute__((aligned(N)))` do for a variable?"
description: "Guarantees that the variable's address is a multiple of N bytes."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
uint8_t buf[64] __attribute__((aligned(32)));
```

## Short answer

**Guarantees that the variable's address is a multiple of N bytes.**

Used for DMA buffers, cache-line alignment, and special memory regions. It is a GCC/Clang extension; the standard equivalent is `_Alignas(N)`.

Rule: `aligned` increases alignment; `packed` reduces padding. They can be combined for wire/DMA descriptors that need both a dense layout and an aligned base address.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
