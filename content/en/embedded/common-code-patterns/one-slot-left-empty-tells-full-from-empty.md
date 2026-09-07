---
id: emb-patterns-0010
title: "How are full and empty distinguished in a ring buffer without a counter?"
description: "Full and empty are distinguished by head and tail with one slot always left empty."
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

**Empty: `head == tail`. Full: `(head + 1) & MASK == tail`** (one slot is always left empty).

This avoids a shared `count` variable that creates a read-modify-write race between the ISR (interrupt service routine) and main.

Rule: one slot is sacrificed, but true lock-free safety is gained without critical sections.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
