---
id: emb-dtypes-0009
title: "Why use `stdint.h` types instead of plain `int`, `short`, `long`?"
description: "stdint.h uintN_t types have an exact width when provided; the implementation determines int/short/long sizes."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 4
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

The sizes and ranges of `int`, `short`, and `long` are specified by the C implementation, so they should not be assumed to match across ABIs. The `<stdint.h>` types `uintN_t`, when provided, have exactly N bits and no padding bits; these exact-width typedefs are optional if the implementation lacks a matching type. For protocols and bit fields, choose a type for the required width and specify representation and byte order separately.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
