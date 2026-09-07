---
id: emb-align-0002
title: "Why does a CPU require aligned data at all?"
description: "The bus reads and writes memory in word-aligned chunks of fixed size"
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

**The bus reads and writes memory in word-aligned chunks of fixed size.**

An aligned access fits in one word -> one transaction. A misaligned value straddles a word boundary -> two transactions plus stitching, or the hardware forbids the access altogether.

Rule: on simpler cores (Cortex-M0) this is not "slower" but a <span class="warn">HardFault</span>; on M3/M4 it is a cycle penalty.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
