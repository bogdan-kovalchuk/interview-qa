---
id: emb-cemb-0002
title: "How do you work with `void`?"
description: "void denotes absence of type and is used for functions with no return, functions with no parameters, and the generic void pointer that cannot be dereferenced without a cast."
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

`void` means "absence of type". Three uses:

1. **Function with no return**: `void init(void);`
2. **Function with no parameters**: `int get(void);` – in C, `int f()` and `int f(void)` differ!
3. **Generic pointer**: `void *ptr` – a pointer to any object type; it cannot be directly dereferenced or used in standard pointer arithmetic.

In C, `void *` implicitly converts to an object pointer, but before access you need a concrete type: `int *p = ptr;`. In C++ such a conversion requires an explicit cast.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
