---
id: emb-volconst-0003
title: "Name three mandatory use cases for `volatile` in embedded C."
description: "Three classic use cases: memory-mapped hardware registers, variables shared with an ISR, and memory modified by DMA."
track: embedded
section: volatile-and-const
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

Three classic use cases: memory-mapped hardware registers, variables shared with an ISR, and memory modified by DMA.

In all three cases the compiler does not see an ordinary C write that changes the value. Without `volatile` it may cache the old value or remove the access as redundant.

Rule: if the source of a value change is invisible to the compiler in the current control flow, consider `volatile`; if the problem is about mutual exclusion or atomicity, `volatile` alone is not enough.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
