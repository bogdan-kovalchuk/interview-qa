---
id: emb-dtypes-0037
title: "What is the difference between `uint32_t` and `unsigned int` for portability?"
description: "unsigned int is at least 16 bits, while uint32_t exists only on implementations with an exact 32-bit unsigned type."
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

`unsigned int` is at least 16 bits, and its width depends on the implementation; the C standard does not tie it to an MCU name.[^iso-c-n1570] `uint32_t` is available only when an implementation has an unsigned integer type exactly 32 bits wide with no padding bits, and then it has that width.[^iso-c-n1570] Use an exact-width type for protocol fields and registers when available and required by the specification; use `size_t` for object sizes.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
