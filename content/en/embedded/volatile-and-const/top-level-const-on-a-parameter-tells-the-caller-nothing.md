---
id: emb-volconst-0041
title: "Why is `void f(uint8_t * const p)` a weak API contract?"
description: "The const here is top-level and applies only to the local copy of the pointer parameter inside the function."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**Because `const` here is top-level and applies only to the local copy of the pointer parameter inside the function.**[^iso-c-n1570]

The caller sees no difference: the pointer value is already passed by value. The function cannot change the pointer at the caller side regardless of `const`. But it can still modify `p[0]` because the pointed-to data is not const.

Rule: if you want to promise that the buffer will not be modified through this pointer, write `void f(const uint8_t *p)`, not `uint8_t * const p`.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
