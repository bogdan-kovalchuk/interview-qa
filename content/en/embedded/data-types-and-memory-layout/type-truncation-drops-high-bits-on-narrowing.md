---
id: emb-dtypes-0039
title: "What is type truncation, and when does it happen?"
description: "Narrowing an integer can change its value; conversion to uint8_t yields the value modulo 256."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
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

Narrowing an integer can change its value; conversion to an unsigned integer type yields the value modulo `U_MAX + 1`.[^iso-c-n1570] For example, where 8-bit `uint8_t` exists, converting `300` produces `44`, because `300 mod 256 = 44`.[^iso-c-n1570] This conversion can occur on assignment, argument passing, or return when the destination type is narrower. Check the range first when losing value is not intended.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
