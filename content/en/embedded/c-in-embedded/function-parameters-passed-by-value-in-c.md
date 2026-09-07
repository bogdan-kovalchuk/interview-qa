---
id: emb-cemb-0007
title: "How are parameters passed to a function?"
description: "In C, parameters are passed by value; to modify or avoid copying, pass an address or, in C++, a reference."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
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

In C, parameters are passed **by value**: the function receives a copy of the argument.[^dou-embedded-interview] If you pass `int x`, modifying the parameter inside the function does not change the caller's variable.

To let a function modify an object or avoid copying a large one, pass its address: `void f(int *p)` or `void g(struct Big *s)`. Arrays in parameters actually decay to a pointer to the first element, so the array size must be passed separately. In C++ there are also references: `T&` and `const T&`.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
