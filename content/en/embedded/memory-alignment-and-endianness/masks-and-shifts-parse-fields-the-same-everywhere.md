---
id: emb-align-0036
title: "Why are masks and shifts on a `uint32_t` more portable than unions or bitfields for parsing fields?"
description: "Arithmetic shifts and masks produce the same result regardless of endianness and compiler."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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

## Short answer

**Arithmetic shifts and masks produce the same result regardless of endianness and compiler.**

`(reg >> 4) & 0x7` always extracts the same logical bits of the value, whereas union overlays and bitfields depend on the platform's byte and bit order.

Rule: for register decode and protocol parsing, work with the value through shift and mask, not with its byte layout in memory.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
