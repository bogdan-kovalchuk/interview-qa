---
id: emb-dtypes-0059
title: "What does `const` mean in `const uint32_t *p` vs `uint32_t * const p`?"
description: "const before the type protects the pointed-to data; const after the protects the pointer's address itself."
track: embedded
section: data-types-and-memory-layout
level: middle
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

`const uint32_t *p` is a pointer to a `uint32_t` that cannot be changed through `*p`, but `p` itself can be redirected.

`uint32_t * const p` is a pointer with a fixed address, but the value of `*p` can be changed.

`const uint32_t * const p` prevents changing either the address or the data through that expression.[^iso-c-n1570]

Reading the declaration helps identify which level `const` qualifies. For a register pointer, `volatile uint32_t * const REG` fixes the address while `volatile` qualifies accesses to the register.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
