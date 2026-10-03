---
id: emb-volconst-0013
title: "What does `volatile const uint32_t * const STATUS` mean?"
description: "STATUS is a const pointer to volatile const uint32t; the address is fixed, data is read-only yet must be reloaded each time."
track: embedded
section: volatile-and-const
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

**`STATUS` is a const pointer to volatile const `uint32_t`**.

The pointer address does not change. Writes through this type are not permitted, while the volatile qualifier applies to accesses to the target object; the C implementation defines the precise access rules. This is a typical type for a read-only status register when that matches the MCU documentation.[^iso-c-n1570]

Rule: `const` prevents modification through this lvalue, while `volatile` qualifies an object that may change in ways unknown to the implementation.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
