---
id: emb-cppfound-0010
title: "What do sizeof(arr) and sizeof(p) return for int arr[8] and int *p = arr?"
description: "sizeof on a real array returns the total byte count while sizeof on a pointer returns only the pointer size, so the same element type yields completely different results."
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

`sizeof(arr)` -> **32** (8 elements × 4 bytes = 32B). `sizeof` on a real array returns the total size in bytes.

`sizeof(p)` -> **4** (or 8 on 64-bit). A pointer stores only an address – its size equals the architecture's word size.

Key difference: array and pointer have the same element type, but `sizeof` gives completely different results.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
