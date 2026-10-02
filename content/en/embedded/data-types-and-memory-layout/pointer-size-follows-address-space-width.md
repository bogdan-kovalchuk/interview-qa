---
id: emb-dtypes-0040
title: "What does `sizeof(void*)` return on a 32-bit versus a 64-bit platform?"
description: "Common 32-bit ABIs use a 4-byte void* and 64-bit ABIs an 8-byte one, but C does not derive these sizes from the architecture label."
track: embedded
section: data-types-and-memory-layout
level: junior
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

Common ABIs use 4-byte `sizeof(void*)` on 32-bit systems and 8 bytes on 64-bit systems, but the C standard does not derive pointer size from an architecture label.[^iso-c-n1570] A platform's address model affects pointer representation, while the implementation determines the exact value. Check `sizeof` with the target toolchain and do not hard-code a size in portable code.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
