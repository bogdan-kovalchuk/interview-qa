---
id: emb-dtypes-0089
title: "What is type punning, and when is it undefined behavior in C++?"
description: "In C, type punning through a union is accepted; in C++ only memcpy or std::bitcast is safe."
track: embedded
section: data-types-and-memory-layout
level: middle
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Type punning** – reading an object of one type through a pointer/reference of another type. In **C**, via `union` – a common and supported technique, but the result depends on the memory representation of the types; via pointer cast (`int x = 1; float *fp = (float*)&x; *fp;`) – <span class="warn">UB (strict aliasing violation)</span>.

In **C++**, only `memcpy` or `std::bit_cast` (C++20) gives safe type punning, whereas `reinterpret_cast` + dereference -> UB. The compiler optimizes code assuming aliasing does not occur.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
