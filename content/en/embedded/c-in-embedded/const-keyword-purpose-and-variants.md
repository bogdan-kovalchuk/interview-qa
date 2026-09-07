---
id: emb-cemb-0012
title: "What is the purpose of the const keyword?"
description: "const prohibits modifying a value through the qualified name after initialization; in embedded it does not guarantee placement in Flash."
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

It prohibits changing the value through that name after initialization.[^dou-embedded-interview] The compiler will issue an error on an attempt to write.

Variants: `const int x = 5;` – constant variable; `const int *p` – pointer to constant (data is protected); `int * const p` – constant pointer (address is protected); `const int * const p` – both are protected.

In embedded, `const` does not guarantee a specific storage location. In many toolchains such data is placed in `.rodata` in Flash, but this depends on the ABI, linker script, and platform; in C++ methods: `void get() const` – guarantees that the method does not change the object's state.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
