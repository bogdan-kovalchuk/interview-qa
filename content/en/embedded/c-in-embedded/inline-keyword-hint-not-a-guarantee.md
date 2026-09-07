---
id: emb-cemb-0013
title: "What does the inline keyword mean?"
description: "inline is a hint and linkage rule that allows a function definition in a header; the optimizer may inline the body but is not required to."
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

`inline` is a hint and a linkage/ODR rule for a function that can be defined in a header.[^dou-embedded-interview] The optimizer may substitute the function body at the call site to eliminate call overhead, but is **not required** to do so.

In C/C++ the semantics differ slightly, but the practical idea is the same: small functions, often helpers or getters, can be made `static inline` in headers. For large functions `inline` usually does not help. It is important not to confuse: the real inlining decision is made by the compiler, while the keyword also affects the permissibility of multiple definitions across translation units.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
