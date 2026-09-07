---
id: emb-patterns-0011
title: "Trap: why does a `count` field in a ring buffer create a race condition?"
description: "ISR increments count and main decrements it, creating a read-modify-write race on a shared variable."
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

<span class="warn">ISR (interrupt service routine) increments `count`, main decrements – this is a read-modify-write on a shared variable.</span>

`count++` is not atomic (read, modify, write); if the ISR preempts main between these steps, an update is lost -> off-by-one and corrupted buffer state.

Mitigation: either a critical section/atomic, or drop `count` entirely – determine full/empty from `head`/`tail` alone.[^embeddedinterviewlab]

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
