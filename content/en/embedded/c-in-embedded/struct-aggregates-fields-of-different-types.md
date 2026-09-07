---
id: emb-cemb-0008
title: "What is a struct?"
description: "A struct groups fields of different types under one name and is used for data objects, protocol packets, and register maps."
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

`struct` is an aggregate type that groups several fields of different or identical types under one name.[^dou-embedded-interview] Unlike an array, fields can have different types: `struct Point { int x; int y; };`.

Structs are used to model data objects, protocol packets, configurations, table records, descriptors, and register maps. Field access: `s.x` for an object and `p->x` for a pointer to a struct. The size of a struct can be larger than the sum of its fields due to padding and alignment.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
