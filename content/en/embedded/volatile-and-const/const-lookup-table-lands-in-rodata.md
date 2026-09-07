---
id: emb-volconst-0025
title: "Which section does a `const` lookup table land in?"
description: "A const table lands in .rodata in Flash when it is file-scope or static and the linker script makes no special exceptions."
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
const uint16_t sine_lut[256] = { 0, 402, 804 };
```

## Short answer

Into `.rodata` in Flash, if it is a file-scope or static object and the linker script makes no special exceptions.

The array is read-only, so startup code does not have to copy it into RAM. For Cortex-M this saves RAM and startup time. The size here is about `256 * 2 = 512` bytes that do not occupy SRAM.

Rule: large immutable tables must be `const`, otherwise they may end up in `.data`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
