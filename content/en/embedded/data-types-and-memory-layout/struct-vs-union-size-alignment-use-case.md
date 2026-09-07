---
id: emb-dtypes-0110
title: "How do struct and union differ in size, alignment, and use-case?"
description: "A struct stores fields sequentially with padding, while a union shares memory among members; struct suits state or register maps, union suits mutually exclusive variants but not safe wire parsing."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

`struct` stores all fields sequentially with possible padding, so its size is roughly the sum of fields plus alignment. `union` shares one block of memory among members, so its size equals the largest member with the required alignment. A struct suits state records or register maps; a union suits mutually exclusive data variants, but not safe wire-format parsing.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
