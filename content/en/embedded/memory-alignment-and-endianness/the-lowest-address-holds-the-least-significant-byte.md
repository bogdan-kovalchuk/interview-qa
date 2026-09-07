---
id: emb-align-0035
title: "What does this code print on a little-endian machine?"
description: "44, because on little-endian the least significant byte sits at the lowest address."
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
uint32_t w = 0x11223344;
uint8_t *p = (uint8_t*)&w;
printf("%02X", p[0]);
```

## Short answer

**`44`**.

On little-endian the least significant byte sits at the lowest address, so `p[0]` is the LSB `0x44`. On big-endian it would print `11`.

Rule: accessing individual bytes through `uint8_t*` is the typical way to "see" endianness; the result depends on the platform.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
