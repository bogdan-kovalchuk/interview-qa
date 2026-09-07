---
id: emb-cemb-0006
title: "What is the size of a union?"
description: "A union size equals its largest member plus padding for the strictest alignment requirement; verify with sizeof."
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

The size of a `union` equals the size of its largest field plus possible padding to satisfy the strictest alignment requirement among the fields.[^dou-embedded-interview] That is, a union must be large enough and properly aligned for any of its members.

For example, `union U { char c[5]; float f; };` may have size 8: the largest field takes 5 bytes, but `float` requires alignment of 4, so padding is added. The exact value is always checked with `sizeof(union U)`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
