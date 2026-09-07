---
id: emb-dtypes-0009
title: "Why use `stdint.h` types instead of plain `int`, `short`, `long`?"
description: "stdint.h types guarantee an exact width across platforms, unlike plain int/short/long."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

The sizes of `int`, `short`, `long` depend on the platform and ABI: `int` is 2 bytes on MSP430, 4 bytes on Cortex-M.

`<stdint.h>` guarantees exact width: `uint8_t` is always 8 bits, `uint32_t` is always 32 bits.

In embedded: register maps, protocols, struct layout – **always fixed-width types**. "For anything stored in a struct, sent over a protocol, or written to a register – use fixed-width types."[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
