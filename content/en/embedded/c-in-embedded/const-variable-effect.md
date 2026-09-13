---
id: emb-cemb-0022
title: "How does `const` affect a variable?"
description: "const gives access through a const-qualified name read-only semantics, but does not guarantee physical placement in Flash or ROM."
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

`const` sets read-only semantics for the compiler: after initialization the object cannot be modified through the const-qualified name, as in `const int x = 5;`. It does not guarantee the data sits in Flash or ROM; placement depends on toolchain, linker script and platform.

Read pointers right to left: `const int *p` – pointer to constant data; `int * const p` – constant pointer; `const int * const p` – both. `const` is not always a compile-time constant and a cast can remove it, but writing to a truly const object is undefined behavior.[^dou-embedded-interview]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
