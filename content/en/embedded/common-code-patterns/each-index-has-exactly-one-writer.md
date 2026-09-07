---
id: emb-patterns-0041
title: "Which shared invariant makes an SPSC ring buffer safe without locks?"
description: "Each index has exactly one writer: the producer writes only head, the consumer writes only tail."
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

**Each index has exactly one writer: the producer writes only `head`, the consumer – only `tail`.**

Since there is no shared variable modified by both sides (like `count`), there is no read-modify-write race either. Reading the other side's index is safe provided it is `volatile` and updated atomically for that MCU (microcontroller unit).

Rule: "one writer per variable" is the foundation of all lock-free SPSC (single-producer / single-consumer) structures.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
