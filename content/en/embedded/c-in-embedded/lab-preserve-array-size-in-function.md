---
id: emb-cppfound-0062
title: "How can an array be passed to a function while preserving its size?"
description: "Ways to preserve array length when array-to-pointer decay removes it."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

Since an array decays to a pointer, the size is <span class="warn">not passed automatically</span>. Options:

1) **Explicit parameter**: `void f(int *arr, size_t n)` – simplest;
2) **Sentinel value**: null-terminator for strings, a special value;
3) **Struct + array**: `struct { int *data; size_t len; }`;
4) C++ **std::span** or `std::array<int,N>`.

Protection: `_Static_assert(sizeof(arr) != sizeof(int*), "Use real array")` at the caller.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
