---
id: emb-structs-0049
title: "Trap: can a bit-field be used as an atomic flag between an ISR and main?"
description: "Bit-field writes are read-modify-write of the storage unit and are not atomic."
track: embedded
section: structs-unions-and-bitfields
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

<span class="warn">Do not.</span>

Writing a bit-field is typically a read-modify-write of the storage unit. If the ISR and main modify different bit-fields in the same storage unit, one write can clobber the other. `volatile` does not make this operation atomic.

Mitigation: for ISR flags, use separate volatile byte/word flags, atomic masks with a critical section, or RTOS event flags.[^embeddedinterviewlab]

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
