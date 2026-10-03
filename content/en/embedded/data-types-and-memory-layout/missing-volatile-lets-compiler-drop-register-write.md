---
id: emb-dtypes-0098
title: "What happens with `uint32_t *ptr = (uint32_t*)0x40020000; *ptr = 0xFF;` without `volatile`?"
description: "Without volatile, the compiler may eliminate the write as a dead store, since nothing reads the pointer again."
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

The compiler may optimize the write as an ordinary memory access because an external device is not part of C’s abstract machine.[^iso-c-n1570]

Without `volatile`, there is no guarantee that the intended write is preserved as a hardware access.

For a memory-mapped register, use a pointer to a `volatile` type, such as `volatile uint32_t *reg`; this requires the relevant accesses under C’s rules, but does not by itself guarantee the correct address, atomicity, or required ordering.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
