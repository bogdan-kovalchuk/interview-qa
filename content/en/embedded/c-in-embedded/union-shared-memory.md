---
id: emb-cemb-0024
title: "What is a `union`?"
description: "A union stores all members in one memory region, so writing one member overwrites bytes shared with the other members."
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

`union` is a type where all members share the same memory region. At any given time, logically one member is active, and writing to one member overwrites bytes that could be used by other members.

Example: `union U { uint32_t word; uint8_t bytes[4]; };`. Used for saving memory, variant data, and low-level access to byte representation. One must be careful with type punning, endianness, alignment, and the rules for the active member, especially in C++.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
