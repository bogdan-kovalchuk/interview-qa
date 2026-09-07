---
id: emb-patterns-0042
title: "What should a candidate be able to do on embedded code pattern questions?"
description: "Write FSMs in both forms, explain trade-offs, build a power-of-two ring buffer, and do unsigned mask-and-shift bit ops."
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

**Write an FSM (finite state machine) in both forms – switch and table; explain the trade-offs; build a power-of-two ring buffer with the `count` race; perform bit operations via unsigned mask-and-shift.**

Plus: consistent return codes with every result checked, `volatile` for registers, guard clauses for null/range.

Rule: for every pattern have answers for "when to apply", "is it ISR-safe (interrupt service routine safe)" and "why no heap".[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
