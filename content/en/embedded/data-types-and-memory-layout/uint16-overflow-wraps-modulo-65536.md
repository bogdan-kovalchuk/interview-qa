---
id: emb-dtypes-0030
title: "What does this return? `uint16_t x = 60000; x += 10000;`"
description: "Unsigned overflow is defined as modular arithmetic, so 60000+10000 gives 4464 rather than undefined behavior."
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

After `x += 10000`, `x` is `4464`: `uint16_t` ranges from `0..65535`, and conversion back reduces 70000 modulo 65536.[^iso-c-n1570]

Unsigned arithmetic is modular, but the path depends on integer promotions: with 32-bit `int`, addition produces 70000 and assignment reduces it; with 16-bit `int`, operands may promote to `unsigned int` and wrap during addition. Either way this yields 4464, not undefined behavior.[^iso-c-n1570]

But if `70000` was expected, it is a bug from the wrong type choice; use `uint32_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
