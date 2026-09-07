---
id: emb-cppfound-0039
title: "What does `memcpy(dst, src, sizeof(src))` do when `src` is an array parameter?"
description: "Why sizeof on an array parameter copies only pointer-sized data."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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

<span class="warn">It copies only 4 or 8 bytes</span> (the pointer size), not the array size.

In a function parameter, `src` is `uint8_t*`, not an array. `sizeof(src) = sizeof(uint8_t*) = 4`. So `memcpy` copies only 4 bytes instead of N.

Correct approach: pass the size explicitly: `memcpy(dst, src, n * sizeof(src[0]))` or `memcpy(dst, src, n)` where `n` is a separate parameter.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
