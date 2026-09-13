---
id: emb-patterns-0013
title: "Why are the fields of a ring buffer struct marked `volatile`?"
description: "head and tail are modified in one context and read in another, so volatile prevents the compiler from caching them."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-09-13
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

**Because `head` and `tail` are modified in one context (ISR) and read in another (main).**

Without `volatile` the compiler can cache the index in a register and miss the other side's update, breaking the full/empty logic. The buffer itself is often not `volatile` if the order “write byte -> publish `head`” holds; volatile is needed for the shared control state.

Rule: indexes and flags shared between ISR (interrupt service routine) and main are `volatile`, but `volatile` gives no atomicity - it only prevents caching of the access.[^embeddedinterviewlab]
## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
