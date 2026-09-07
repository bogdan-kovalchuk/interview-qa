---
id: emb-align-0033
title: "Why is `memcpy` safer than a typed-pointer cast for multi-byte access?"
description: "memcpy has no alignment requirement and does not violate strict aliasing."
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

**`memcpy` has no alignment requirement** for source or destination and does not violate strict aliasing.

The compiler optimizes a fixed-size `memcpy` into efficient load/store operations (and on M0 into safe byte-wise accesses), so you get both correctness and speed.

Rule: for unaligned reads and writes of multi-byte values, `memcpy` is the standard portable tool.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
