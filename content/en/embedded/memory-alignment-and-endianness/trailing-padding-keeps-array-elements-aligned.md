---
id: emb-align-0006
title: "Why does a struct need trailing padding?"
description: "Trailing padding ensures every element in an array of structs starts at an aligned address"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**So that in an array of structs every subsequent element is also aligned.**

If `sizeof(struct)` is not a multiple of the largest field's alignment, then `arr[1]` would start at a misaligned address and accesses to its fields would be misaligned. That is why the compiler rounds the size up to a multiple.

Rule: trailing padding is exactly why `sizeof` a struct is not the sum of its fields.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
