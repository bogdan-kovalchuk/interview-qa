---
id: emb-align-0011
title: "What are little-endian and big-endian for the value `0x12345678`?"
description: "Byte order of a multi-byte value in memory determines whether the least or most significant byte comes first"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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

**Byte order of a multi-byte value in memory.**

```text
Адреса:  00   01   02   03
LE:      78   56   34   12  (little-endian, LSB перший)
BE:      12   34   56   78  (big-endian, MSB перший)
```

LSB (least significant byte) is the lowest byte, MSB (most significant byte) is the highest byte. Little-endian: the lowest byte at the lowest address (ARM default, x86, RISC-V). Big-endian: the highest byte first (PowerPC, 68k, network).

Rule: endianness affects only multi-byte types; a `uint8_t` array is the same everywhere.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
