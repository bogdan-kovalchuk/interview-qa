---
id: emb-volconst-0029
title: "What is the MISRA approach to `const` for pointer parameters?"
description: "A pointer parameter should point to a const-qualified type if the function does not modify the pointed-to object."
track: embedded
section: volatile-and-const
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

**A pointer parameter should point to a const-qualified type if the function does not modify the pointed-to object.**

The idea is not about style but about contract: a static analyzer can distinguish a read-only input buffer from an output buffer. This prevents accidental writes to Flash tables, string literals, or DMA descriptors that must be immutable for that function.

Practical rule: `void parse(const uint8_t *frame, size_t len)` is better than `void parse(uint8_t *frame, size_t len)` if the parser does not modify the frame.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
