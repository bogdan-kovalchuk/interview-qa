---
id: emb-structs-0010
title: "Why must the fields of a peripheral register struct be `volatile`?"
description: "Because each field represents a hardware register whose value can change outside C code or have side effects on read or write."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: concept
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

**Because each field represents a hardware register whose value can change outside C code or have side effects on read or write.**

Without `volatile`, the compiler may cache a status bit, eliminate a read of a read-to-clear register, or merge writes. On Cortex-M this is a typical cause of bugs that appear only in release builds.

Rule: a register overlay must have volatile-qualified fields or access through a pointer to a volatile register type.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
