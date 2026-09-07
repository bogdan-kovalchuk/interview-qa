---
id: emb-align-0043
title: "What should a candidate demonstrate on alignment and endianness questions?"
description: "Predict padding and reorder fields, explain endianness, use htonl/ntohl correctly, serialize field by field, and understand the cost of packed and misaligned access."
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

**Predict padding and reorder fields, explain endianness, and use `htonl`/`ntohl` correctly.**

A strong answer also covers: field-by-field serialization instead of raw `struct`, understanding the cost of `packed`, and the risk of HardFault on M0 / penalty on M3/M4 for misaligned access.

Rule: talk about explicit wire format and explicit byte order – this is a marker of embedded systems experience.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
