---
id: emb-cppfound-0089
title: "What is the difference between memcpy and a pointer cast for copying between types?"
description: "Why memcpy avoids aliasing and alignment problems during type punning."
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Pointer cast + dereference**: `uint32_t x = *(uint32_t*)bytes;` – potential UB (strict aliasing, misalignment). The compiler may optimize "incorrectly".

**memcpy**: `uint32_t x; memcpy(&x, bytes, 4);` – always correct: does not violate aliasing, the compiler optimizes it to a single LDR if aligned.

Rule: for type punning use `memcpy` (or `union` in C). Pointer cast is safe only for `char*`/`unsigned char*`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
