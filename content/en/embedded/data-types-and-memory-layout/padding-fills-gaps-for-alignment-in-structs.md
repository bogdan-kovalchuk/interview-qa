---
id: emb-dtypes-0024
title: "What is padding in structs, and where does it come from?"
description: "Implementations may insert padding between or after struct members to satisfy target alignment requirements."
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

Padding is space an implementation may insert between or after struct members to satisfy alignment requirements. For an ABI where `char` has size 1 and `int` requires four-byte alignment, `struct { char c; int x; }` places `x` at offset 4, with three bytes between the members. Exact offsets and total size depend on the implementation and ABI; they are not universal C guarantees.[^iso-c-n1570][^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
