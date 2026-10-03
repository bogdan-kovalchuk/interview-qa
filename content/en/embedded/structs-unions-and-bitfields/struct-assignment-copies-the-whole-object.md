---
id: emb-structs-0039
title: "How do assignment and `memcpy` differ for structs?"
description: "Structure assignment copies every member value; padding bytes have no guaranteed value."
track: embedded
section: structs-unions-and-bitfields
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

**Structure assignment copies every struct member value**, but does not guarantee preservation of padding bytes.

`memcpy` copies the object representation byte by byte, including padding. The C standard allows padding bytes to take unspecified values when a struct value is stored, so assignment and `memcpy` do not promise the same in-memory representation.

Use assignment to copy a struct in C. For wire or storage serialization, encode fields explicitly instead of relying on padding or compiler-specific layout.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
