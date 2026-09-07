---
id: emb-cemb-0017
title: "What is alignment used for, and can it be controlled?"
description: "Alignment ensures fast and correct CPU data access and can be controlled via field order, alignas, and compiler attributes like packed."
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

Alignment is needed for fast and correct CPU access to data.[^dou-embedded-interview] Many architectures read 2/4/8-byte values more efficiently when the address is a multiple of the type size; some MCUs can generate a fault on misaligned access.

You can control it through field order in a struct, standard `alignas` in C++ or `_Alignas`/`alignas` in modern C, and compiler-specific attributes like `__attribute__((aligned))`, `__attribute__((packed))`, `#pragma pack`. `packed` should be used carefully: it saves bytes but can slow down access or break hardware requirements.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
