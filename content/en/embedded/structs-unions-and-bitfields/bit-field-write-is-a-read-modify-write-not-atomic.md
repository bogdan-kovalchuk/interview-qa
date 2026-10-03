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

Writing a bit-field is typically a read-modify-write of the storage unit, so it should not be used as an atomic flag between an ISR and main. If both contexts modify different bit-fields in the same storage unit, one write can clobber the other. `volatile` does not make this operation atomic.

Mitigation: use separate flags only when accesses are atomic on the target; otherwise use a critical section or RTOS event flags. `volatile` alone guarantees neither atomicity nor synchronization.[^iso-c-n1570]

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
