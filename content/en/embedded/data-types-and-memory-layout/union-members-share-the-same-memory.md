---
id: emb-dtypes-0023
title: "What memory layout does this have? `union { uint32_t word; uint8_t bytes[4]; };`"
description: "Union members overlap; exact size can include padding, and byte order depends on the target."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

Union members overlap the same storage, and the union is large enough for its largest member, with implementation-defined layout and possible padding. On a platform where `uint32_t` is four bytes, this example needs at least four bytes. Reading the bytes after writing `word` exposes a platform representation: byte order is not specified by the union or by C, so the shown sequence applies only to a little-endian target.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
