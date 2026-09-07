---
id: emb-volconst-0002
title: "Which three optimisations does `volatile` usually block?"
description: "volatile blocks caching the value in a register, eliminating redundant accesses, and reordering relative to other volatile accesses."
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

**`volatile` blocks caching the value in a register, eliminating redundant accesses, and reordering relative to other volatile accesses.**

Without it, the compiler might read a flag once, remove the first of two writes to a hardware register, or reorder accesses so the peripheral sees the wrong sequence. In embedded this is not just a micro-optimisation: every read or write of a register address can have a side effect.

Rule: if an access has a hardware side effect or the value can change asynchronously, the object type must be volatile-qualified.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
