---
id: emb-cppfound-0077
title: "What is the strict aliasing rule, and how does it apply to pointer casts?"
description: "How strict aliasing constrains accesses through incompatible pointer types."
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Strict aliasing rule** (C99 §6.5): the compiler may assume that pointers of different incompatible types do NOT alias (do not point to the same memory area). This allows aggressive optimization: if modified through `float*` – the compiler is not required to re-read through `int*`. Exception: `char*` and `unsigned char*` may alias anything. Violation: `int x; float *fp=(float*)&x; *fp=1.0f;` -> UB; protection: `memcpy` or `union` (in C).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
