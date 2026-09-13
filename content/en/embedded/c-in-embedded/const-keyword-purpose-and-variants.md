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
updated: 2026-09-13
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

It forbids changing the value through that name after initialization, and a write attempt is a compile error.[^dou-embedded-interview]

Variants: `const int x = 5;` – constant variable; `const int *p` – pointer to constant (data protected); `int * const p` – constant pointer (address protected); `const int * const p` – both protected.

In embedded, `const` guarantees no particular storage location: many toolchains put such data in `.rodata` in Flash, but that depends on the ABI, linker script and platform. On C++ methods, `void get() const` guarantees the method does not change the object's state.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
