---
id: emb-align-0028
title: "Trap: why is `sizeof(struct)` not the sum of its field sizes?"
description: "Padding may appear between fields and at the end of a struct; exact layout depends on the ABI."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">Because of padding</span> between fields to meet their alignment and at the end to preserve struct alignment in arrays. Exact layout depends on the ABI and implementation.

For an ABI with alignments of 1, 4, and 2 bytes, `{uint8_t; uint32_t; uint16_t;}` uses 1 + 3 padding + 4 + 2 + 2 trailing padding = 12 bytes, not 7.[^iso-c-n1570]

Guard: for layout analysis always use `sizeof` and `offsetof`; do not sum fields in your head.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
