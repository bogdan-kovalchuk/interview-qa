---
id: emb-cemb-0015
title: "How is const-correctness for variables handled?"
description: "Const-correctness is part of the type; the compiler enforces it at access time, and casting away const on a truly const object is undefined behavior."
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

Const-correctness is part of the type that the compiler checks during access validation.[^dou-embedded-interview] If an object or parameter is declared `const`, writing through that path is prohibited: `void f(const int *p)` can read `*p` but not modify it.

In C++ `const` is also used for methods: `int get() const` means the method does not change the logical state of the object. You can remove const through a cast, but if the original object was truly const, writing leads to undefined behavior. Good practice: put `const` on input data that the function does not modify.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
