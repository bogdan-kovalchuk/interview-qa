---
id: emb-align-0003
title: "Which two rules determine the padding in a struct?"
description: "Each field is aligned to its natural alignment and the struct size is a multiple of the largest field alignment"
track: embedded
section: memory-alignment-and-endianness
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

1. Each field sits at an address that is a multiple of its natural alignment (padding is inserted between fields). 2. The total size of the struct is a multiple of the largest field's alignment (trailing padding) – so that in an array of structs every element is also aligned.

Rule: `sizeof(struct)` ≠ the sum of field sizes; always account for both internal and trailing padding.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
