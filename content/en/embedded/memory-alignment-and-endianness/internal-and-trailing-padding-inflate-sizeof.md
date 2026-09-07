---
id: emb-align-0028
title: "Trap: why is `sizeof(struct)` not the sum of its field sizes?"
description: "Because of internal padding for field alignment and trailing padding to match the largest alignment."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
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

<span class="warn">Because of padding</span>, both internal (to align fields) and trailing (to make the size a multiple of the largest alignment).

Example: `{uint8_t; uint32_t; uint16_t;}` = 1 + 3 pad + 4 + 2 + 2 pad = 12, not 7.

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
