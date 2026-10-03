---
id: emb-volconst-0010
title: "What does the declaration `uint32_t * volatile p` mean?"
description: "p is a volatile pointer to plain uint32t; volatile qualifies the pointer value, not the data at the address."
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

**`p` is a volatile pointer to a plain `uint32_t`**.

Here volatile applies to the pointer variable itself, not to the data at the address. Access to `p` is volatile, but `*p` designates an ordinary `uint32_t`, not volatile hardware data.[^iso-c-n1570]

For volatile data at the address, use `volatile uint32_t *p`; for both properties, use `volatile uint32_t * volatile p`.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
