---
id: emb-cemb-0005
title: "How do you determine the size of a struct?"
description: "Use sizeof to get the struct size including padding, and offsetof from stddef.h to inspect the layout; exact size depends on ABI, compiler, packing, and field order."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

The size of a struct is determined by the `sizeof(struct_type)` operator or `sizeof variable`.[^dou-embedded-interview] It includes all fields, internal padding between them, and possible trailing padding at the end so that an array of such structs has correct alignment for every element.

For layout analysis, use `offsetof(struct_type, field)` from `<stddef.h>`. Example: `struct S { char c; int x; };` often has size 8 rather than 5 because `int` is aligned to 4 bytes. The exact size depends on the ABI, compiler, packing options, and field order.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
