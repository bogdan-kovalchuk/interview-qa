---
id: emb-patterns-0031
title: "Why is `volatile` not enough for a safe `count++` between an ISR and main?"
description: "volatile prevents caching but does not make the operation atomic"
track: embedded
section: common-code-patterns
level: junior
type: pitfall
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

<span class="warn">`volatile` prevents caching but does NOT make the operation atomic.</span>

`count++` is a read-modify-write (RMW, 3 steps); an ISR (interrupt service routine) can preempt main in the middle, and the increment is lost. `volatile` only guarantees that each step goes to memory, not that the steps are indivisible.

Defense: a critical section, an atomic type, or a design without shared RMW (head/tail-only ring buffer).[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
