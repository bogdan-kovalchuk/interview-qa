---
id: emb-align-0037
title: "Why enable `UNALIGN_TRP` on an M3/M4 during development?"
description: "To turn hidden misaligned accesses into an explicit fault instead of a silent penalty."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

**To turn hidden misaligned accesses into an explicit fault instead of a silent penalty.**

By default M3/M4 can "forgive" some misaligned accesses, so a bug that would break an M0 port or become undefined behavior through a typed-pointer cast in C goes unnoticed. `UNALIGN_TRP` (a bit in `SCB->CCR`, System Control Block -> Configuration and Control Register) makes such errors visible earlier.

Rule: enable the trap in a debug build to catch portable alignment bugs before moving to a smaller core.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
