---
id: emb-align-0020
title: "Trap: why can you not `memcpy` a raw struct between different MCUs?"
description: "Different compilers and architectures produce different padding and byte order so raw memcpy sends an incompatible layout"
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

<span class="warn">Different compilers and architectures produce different padding and byte order for the same code.</span>

One side may have different field offsets and opposite endianness, so the same `struct` looks different in memory. A raw `memcpy` would transfer an incompatible layout.

Fix: always define an explicit wire format and serialize field by field with explicit byte order.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
