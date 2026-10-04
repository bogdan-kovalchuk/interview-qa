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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">The ISR (interrupt service routine) increments `count` while main decrements it; these operations can conflict.</span>

`count++` and `count--` are read, compute, and write sequences, not guaranteed atomic operations; an interrupt can occur between those steps and overwrite an update.

The result is incorrect capacity accounting: the buffer may appear full or empty incorrectly. Use a critical section, a suitable atomic mechanism, or a design without a shared `count`.[^iso-c-n1570]

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
