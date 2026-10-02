---
id: emb-dtypes-0045
title: "What happens? `unsigned char x = 0; x--;`"
description: "Unsigned arithmetic is defined as modular, so 0-1 gives 255 rather than undefined behavior."
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

After `x--`, `x` is **255** if `unsigned char` has 8 bits; C does not require it to be 8 bits. Integer promotions apply to the subtraction, then conversion on assignment reduces the result modulo `UCHAR_MAX + 1`.[^iso-c-n1570]

This conversion is defined, not signed overflow. A condition such as `i >= 0` is always true for an unsigned value, so a loop using it will not terminate by decrementing to zero.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
