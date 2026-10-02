---
id: emb-dtypes-0078
title: "How does the compiler lay this out? `struct { uint8_t a; uint8_t b; uint16_t c; uint32_t d; }`"
description: "On a common ABI this order can produce an 8-byte struct with no padding, but the actual layout is implementation-dependent."
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

On a common ABI where `uint16_t` has alignment 2 and `uint32_t` alignment 4, the structure can have offsets 0, 1, 2, and 4 and a size of 8 bytes.[^iso-c-n1570] However, C leaves member alignment to the implementation, so the standard does not guarantee this layout or the absence of padding on every platform. Check `sizeof` and `offsetof` with the target toolchain.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
