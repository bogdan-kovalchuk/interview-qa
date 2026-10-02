---
id: emb-dtypes-0020
title: "What happens? `int8_t x = 127; x++;`"
description: "Overflowing int8t past 127 is undefined behavior in the C standard, though it often wraps to -128 in practice."
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

In `x++`, integer promotions convert `int8_t` to `int`, so `127 + 1` does not overflow `int`; converting 128 back to `int8_t` has an implementation-defined result or signal, rather than undefined behavior.[^iso-c-n1570]

Common implementations yield `-128`, but this is not portable wraparound; by contrast, signed arithmetic that overflows its own type has undefined behavior.[^iso-c-n1570]

Use `uint8_t` for modulo wraparound, and check `x < INT8_MAX` before incrementing when the value must stay in signed range.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
