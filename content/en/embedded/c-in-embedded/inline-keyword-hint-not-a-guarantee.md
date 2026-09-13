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

`inline` is a hint plus a linkage/ODR rule for a function that may be defined in a header.[^dou-embedded-interview] The optimizer may substitute the body at the call site to remove call overhead, but is **not required** to.

C and C++ differ slightly, yet the practical idea is the same: small helpers or getters can be `static inline` in headers, and on large functions `inline` usually does not help. The compiler makes the real inlining decision; the keyword separately governs multiple definitions across translation units.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
