---
id: emb-volconst-0018
title: "What does `const uint8_t * const buf` mean?"
description: "buf is a const pointer to const uint8t; neither the address nor the data through the pointer can be changed."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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

**`buf` is a const pointer to const `uint8_t`**.

Neither the pointer address nor the data through the pointer can be changed. This is useful for a local alias to a read-only table, calibration data, or a read-only memory region.

Rule: the first `const` next to the base type guards the data; `const` after `*` guards the pointer itself.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
