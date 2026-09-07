---
id: emb-patterns-0024
title: "Why must peripheral registers be `volatile`?"
description: "The status register is changed by hardware asynchronously not by code"
track: embedded
section: common-code-patterns
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

**The status register is changed by hardware asynchronously, not by code.**

Without `volatile` the compiler assumes memory changes only through program writes: it may read the register once, cache it in a CPU (central processing unit) register, and never re-read it. `volatile` forces every read and write to go to real memory.

Rule: any memory-mapped register is `volatile`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
