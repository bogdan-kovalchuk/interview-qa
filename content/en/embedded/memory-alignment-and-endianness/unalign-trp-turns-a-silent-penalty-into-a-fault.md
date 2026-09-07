---
id: emb-align-0008
title: "How does a misaligned access behave on Cortex-M3/M4 and what is `UNALIGN_TRP`?"
description: "M3 and M4 allow unaligned accesses at a cycle cost and UNALIGN_TRP turns them into explicit faults"
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

**M3/M4/M7 often allow ordinary unaligned halfword/word accesses, but at a cost in bus cycles**; certain instructions such as `LDM`/`STM` (load/store multiple), `LDRD`/`STRD` (load/store doubleword) still require alignment.

The `UNALIGN_TRP` bit in the `SCB->CCR` register (System Control Block -> Configuration and Control Register) enables a trap for unaligned word/halfword accesses that would otherwise silently run slower. This turns a hidden problem into an explicit fault.

Rule: enable `UNALIGN_TRP` during development to catch misaligned bugs, but do not rely on unaligned typed-pointer access in C – it can still be undefined behavior at the language level.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
