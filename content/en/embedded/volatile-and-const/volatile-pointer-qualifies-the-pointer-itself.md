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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
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

Here volatile applies to the pointer variable itself, not to the data at the address. The compiler must reload the address stored in `p`, but the `*p` access is not a volatile access to hardware data.

Embedded takeaway: for registers you almost always need `volatile uint32_t *p`, not `uint32_t * volatile p`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
