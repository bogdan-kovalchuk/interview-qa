---
id: emb-dtypes-0063
title: "What value does this hold? `uint8_t result = (uint8_t)(200 + 100)`"
description: "The explicit cast truncates the result the same way an implicit assignment would, so result is 44."
track: embedded
section: data-types-and-memory-layout
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

`result = 44`.

`200 + 100` is computed as `int` (integer promotion): `300`; the explicit cast `(uint8_t)` truncates to 8 bits: `300 & 0xFF = 0x2C = 44`.

Difference from implicit: the explicit cast shows awareness of truncation, but the result is the same - 44.

For portable code: check that the value fits in the target type before narrowing.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
