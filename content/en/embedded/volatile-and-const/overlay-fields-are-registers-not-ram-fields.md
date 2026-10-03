---
id: emb-volconst-0045
title: "Why are peripheral register struct fields declared `volatile`?"
description: "Each field of the struct overlay represents a hardware register, not an ordinary RAM field."
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

**Because each field of the struct overlay represents a hardware register, not an ordinary RAM field.**

When code accesses a field declared volatile, the implementation must preserve the corresponding volatile access under the C rules. However, the exact definition of an access is implementation-defined; `volatile` alone does not guarantee atomicity, bus transaction width, or the required ordering of hardware operations.[^iso-c-n1570]

Rule: qualify memory-mapped register accesses as `volatile`, and check the address, field layout, access width, and side effects against the MCU documentation.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->
